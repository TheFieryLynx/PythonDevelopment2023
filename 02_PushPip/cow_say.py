#!/usr/bin/env python3

import argparse
import cowsay
import sys

parser = argparse.ArgumentParser(
					prog = 'Cow say project',
					description = 'The Cowsay program works the same way as the original cowsay program',
)

parser.add_argument('-e', 
					dest = 'eye_string',
					action = 'store',
					required = False,
					default = 'oo',
					help = "The appearance of the cow's eyes, in which case the first two characters of the argument string eye_string will be used"
		)

parser.add_argument('-f', 
					dest = 'cowfile',
					action = 'store',
					required = False,
					default = '',
					help = "Specifies a particular cow picture file (''cowfile'') to use"
		)

parser.add_argument('-l', 
					dest = 'list',
					action = 'store_true',
					required = False,
					help = "List all cowfiles on the current COWPATH, invoke with the -l switch"
		)

parser.add_argument('-n', 
					dest = 'wrap',
					action = 'store_false',
					required = False,
					help = "If it is specified, the given message will not be word-wrapped."
		)

parser.add_argument('-T', 
					dest = 'tongue_string',
					action = 'store',
					required = False,
                    default = "  ",
					help = "The appearance of the cow's eyes. It must be two characters and does not appear by default."
		)

parser.add_argument('-W', 
					dest = 'width',
					action = 'store',
					required = False,
					default = 40,
                    type = int,
					help = "Specifies roughly (where the message should be wrapped. The default is equivalent to -W 40 i.e. wrap words at or before the 40th column."
		)

parser.add_argument('-b', 
					dest = 'preset',
					action = 'append_const',
                    const='b',
                    default=[""],
					required = False,
					help = "Initiates Borg mode"
		)

parser.add_argument('-d', 
					dest = 'preset',
					action = 'append_const',
                    const='d',
                    default=[""],
					required = False,
					help = "Causes the cow to appear dead"
		)

parser.add_argument('-g', 
					dest = 'preset',
					action = 'append_const',
                    const='g',
                    default=[""],
					required = False,
					help = "Invokes greedy mode"
		)
		
parser.add_argument('-p', 
					dest = 'preset',
					action = 'append_const',
                    const='p',
                    default=[""],
					required = False,
					help = "Causes a state of paranoia to come over the cow"
		)
		
parser.add_argument('-s', 
					dest = 'preset',
					action = 'append_const',
                    const='s',
                    default=[""],
					required = False,
					help = "Makes the cow appear thoroughly stoned"
		)

parser.add_argument('-t', 
					dest = 'preset',
					action = 'append_const',
                    const='t',
                    default=[""],
					required = False,
					help = "Yields a tired cow"
		)
		
parser.add_argument('-w', 
					dest = 'preset',
					action = 'append_const',
                    const='w',
                    default=[""],
					required = False,
					help = "Opposite of -t, and initiates wired mode"
		)
		
parser.add_argument('-y', 
					dest = 'preset',
					action = 'append_const',
                    const='y',
                    default=[""],
					required = False,
					help = "Brings on the cow's youthful appearance"
		)

parser.add_argument('message', 
					action = 'store',
                    default = ' ',
                    nargs='?',
					help = "message"
		)
		
args = parser.parse_args()

if args.list:
    print(cowsay.list_cows())
    sys.exit()
    
# If the cowfile spec contains '/' then it will be interpreted as a path relative to the current directory. Otherwise, cowsay will search the path specified in the COWPATH environment variable. To list all cowfiles on the current COWPATH, invoke with the -l switch.
    
if args.cowfile in cowsay.list_cows() and "/" not in args.cowfile:
    cow_arg = args.cowfile
else:
    cow_arg = 'default'
    
if "/" in args.cowfile:
    cowfile_arg = args.cowfile
else:
    cowfile_arg = None
    

print(cowsay.cowsay(message=args.message,
              cow=cow_arg,
              preset=max(args.preset),
              eyes=args.eye_string[0:2],
              tongue=args.tongue_string[0:2],
              width=args.width,
              wrap_text=args.wrap,
              cowfile=cowfile_arg)
)