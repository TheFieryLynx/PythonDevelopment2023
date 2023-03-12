import cmd
import shlex
import cowsay
from dataclasses import dataclass

@dataclass
class Option:
    eyes: str = 'oo'
    tongue: str = '  '

@dataclass
class Bubble:
    stem: str = '\\'
    l: str = '<'
    r: str = '>'
    tl: str = '/'
    tr: str = '\\'
    ml: str = '|'
    mr: str = '|'
    bl: str = '\\'
    br: str = '/'

THOUGHT_OPTIONS = {
        'cowsay': Bubble('\\', '<', '>', '/', '\\', '|', '|', '\\', '/'),
        'cowthink': Bubble('o', '(', ')', '(', ')', '(', ')', '(', ')'),
    }

class Commandline(cmd.Cmd):
    intro = 'The Cowsay program works the same way as the original cowsay program\n'

    def do_exit(self, arg):
        'Quit cowsay'
        return True
    
    def do_list_cows(self, arg):
        print(arg)
        if arg:
            args = shlex.split(arg)[0]
            print(*cowsay.list_cows(args))
        else:
            print(*cowsay.list_cows())

    def do_make_bubble(self, arg):
        '''
        make_bubble text [wrap_text] [width] [brackets]
        make_bubble text [wrap_text] [width]
        make_bubble text [wrap_text]
        make_bubble text
        Wraps text if wrap_text is true, then pads text and sets inside a bubble. This is the text that appears above the cows
        '''
        text, *args = shlex.split(arg)
        brackets = 'cowsay'
        width = 40
        wrap_text = True
        if len(args) == 1:
            wrap_text = args[0]
        elif len(args) == 2:
            wrap_text, width = args
        elif len(args) == 3:
            wrap_text, width, brackets = args
        print(cowsay.make_bubble(text, wrap_text = wrap_text, width = int(width), brackets = THOUGHT_OPTIONS[brackets]))

    def do_cowsay(self, arg):
        '''
        Similar to the cowsay command. Parameters are listed with their
        corresponding options in the cowsay command. Returns the resulting cowsay
        string
        cowsay text [cow] [eyes] [tongue]

        :param message: The message to be displayed
        :param cow: the available cows can be found by calling list_cows
        :param eyes: eye string
        :param tongue: tongue string
        '''
        text, *args = shlex.split(arg)
        cow = 'default'
        eyes = Option.eyes
        tongue = Option.tongue
        if len(args) == 1:
            cow = args[0]
        elif len(args) == 2:
            cow, eyes = args
        elif len(args) == 3:
            cow, eyes, tongue = args
        print(cowsay.cowsay(text, cow = cow, eyes = eyes, tongue = tongue))

    def do_cowthink(self, arg):
        '''
        Similar to the cowthink command. Parameters are listed with their
        corresponding options in the cowsay command. Returns the resulting cowsay
        string
        cowthink text [cow] [eyes] [tongue]

        :param message: The message to be displayed
        :param cow: the available cows can be found by calling list_cows
        :param eyes: eye string
        :param tongue: tongue string
        '''
        text, *args = shlex.split(arg)
        cow = 'default'
        eyes = Option.eyes
        tongue = Option.tongue
        if len(args) == 1:
            cow = args[0]
        elif len(args) == 2:
            cow, eyes = args
        elif len(args) == 3:
            cow, eyes, tongue = args
        print(cowsay.cowthink(text, cow = cow, eyes = eyes, tongue = tongue))

    


if __name__ == '__main__':
    Commandline().cmdloop()
