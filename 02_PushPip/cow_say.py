#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(
					prog = 'Cow say project',
					description = 'The Cowsay program works the same way as the original cowsay program',
					epilog = 'Text at the bottom of help'
		)

parser.add_argument('-e', 
					dest = 'eye string',
					action = 'store',
					required = False,
					default = '',
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
					dest = 'cowfile',
					action = 'store_true',
					required = False,
					help = "List all cowfiles on the current COWPATH, invoke with the -l switch"
		)

parser.add_argument('-n', 
					dest = 'cowfile',
					action = 'store_false',
					required = False,
					help = "If it is specified, the given message will not be word-wrapped."
		)

parser.add_argument('-T', 
					dest = 'tongue_string',
					action = 'store',
					required = False,
					help = "The appearance of the cow's eyes. It must be two characters and does not appear by default."
		)

parser.add_argument('-W', 
					dest = 'width',
					action = 'store',
					required = False,
					default = 40,
					help = "Specifies roughly (where the message should be wrapped. The default is equivalent to -W 40 i.e. wrap words at or before the 40th column."
		)

parser.add_argument('-b', 
					dest = 'b',
					action = 'store_true',
					required = False,
					help = "Initiates Borg mode"
		)

parser.add_argument('-d', 
					dest = 'd',
					action = 'store_true',
					required = False,
					help = "Causes the cow to appear dead"
		)

parser.add_argument('-g', 
					dest = 'g',
					action = 'store_true',
					required = False,
					help = "Invokes greedy mode"
		)
		
parser.add_argument('-p', 
					dest = 'p',
					action = 'store_true',
					required = False,
					help = "Causes a state of paranoia to come over the cow"
		)
		
parser.add_argument('-s', 
					dest = 's',
					action = 'store_true',
					required = False,
					help = "Makes the cow appear thoroughly stoned"
		)

parser.add_argument('-t', 
					dest = 't',
					action = 'store_true',
					required = False,
					help = "Yields a tired cow"
		)
		
parser.add_argument('-w', 
					dest = 'w',
					action = 'store_true',
					required = False,
					help = "Opposite of -t, and initiates wired mode"
		)
		
parser.add_argument('-y', 
					dest = 'y',
					action = 'store_true',
					required = False,
					help = "Brings on the cow's youthful appearance"
		)
		
args = parser.parse_args()