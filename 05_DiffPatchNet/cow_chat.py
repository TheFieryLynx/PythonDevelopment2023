#!/usr/bin/env python3
import asyncio
import cowsay
import uuid

clients = {}
cows_names = cowsay.list_cows()

async def chat(reader, writer):
    uuid_con = str(uuid.uuid1())
    usercowname = ''
    print('New Connection: ' + uuid_con)
    is_reg = False
    queue = asyncio.Queue()
    send = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(queue.get())
    while not reader.at_eof():
        done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)
        for q in done:
            if q is send:
                send = asyncio.create_task(reader.readline())
                message = q.result().decode().split()
                if message[0] == 'who':
                    writer.write('Users:\n'.encode())
                    for i in clients.keys():
                        writer.write(f"{i}\n".encode())
                    await writer.drain()
                elif message[0] == 'cows':
                    writer.write('Free cownames:\n'.encode())
                    for i in cows_names:
                        writer.write(f"{i}\n".encode())
                    await writer.drain()
                elif message[0] == 'login':
                    if is_reg:
                        writer.write('Already registered\n'.encode())
                        await writer.drain()
                    elif len (message) == 1:
                        writer.write('Name is required. (login [name])\n'.encode())
                        await writer.drain()
                    elif not is_reg:
                        if message[1] in cows_names:
                            writer.write("Registered!\n".encode())
                            await writer.drain()
                            print(uuid_con + ' registered as ' + message[1])
                            clients[message[1]] = asyncio.Queue()
                            cows_names.remove(message[1])
                            usercowname = message[1]
                            is_reg = True
                            receive.cancel()
                            receive = asyncio.create_task(clients[message[1]].get())
                        else:
                            writer.write("Wrong name!\n".encode())
                            await writer.drain()
                elif message[0] == 'say':
                    if not is_reg:
                        writer.write('Not registered!\n'.encode())
                        await writer.drain()
                    elif len (message) == 1 or len (message) == 2:
                        writer.write('Name and message are required. (say [dist name] [message])\n'.encode())
                        await writer.drain()
                    elif message[1] in clients.keys():
                        await clients[message[1]].put(f"{cowsay.cowsay(message[2], cow=usercowname)}")
                        writer.write("mooo ^^\n".encode())
                        await writer.drain()
                    else:
                        writer.write(f'Unknown user {message[1]}\n'.encode())
                        await writer.drain()
                elif message[0] == 'yield':
                    if not is_reg:
                        writer.write('Not registered!\n'.encode())
                        await writer.drain()
                    elif len (message) == 1:
                        writer.write('Message is required. (say [message])\n'.encode())
                        await writer.drain()
                    else:
                        for out in clients.values():
                            if out is not clients[usercowname]:
                                await out.put(f"{cowsay.cowsay(message[1], cow=usercowname)}")
                        writer.write("mooo ^^\n".encode())
                        await writer.drain()
                elif message[0] == 'quit':
                    send.cancel()
                    receive.cancel()
                    if is_reg:
                        del clients[usercowname]
                        print(usercowname, "left")
                        cows_names.append(usercowname)
                    else:
                        print(uuid_con, "left")
                    writer.close()
                    await writer.wait_closed()
                    return
                else:
                    writer.write('Unknown command\n'.encode())
                    await writer.drain()
            elif q is receive and is_reg:
                receive = asyncio.create_task(clients[usercowname].get())
                writer.write(f"{q.result()}\n".encode())
                await writer.drain()
    send.cancel()
    receive.cancel()
    print(usercowname, "DONE")
    del clients[usercowname]
    writer.close()
    await writer.wait_closed()
    return

async def main():
    server = await asyncio.start_server(chat, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

asyncio.run(main())