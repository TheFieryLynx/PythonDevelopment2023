#!/usr/bin/env python3

import argparse
import sys
import urllib.request

def dictFilter(l, lst):
	return list(filter(lambda x: len(x) == l, lst))

parser = argparse.ArgumentParser(
	prog = "Bulls and cows",
	description = "03 task",
	formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

parser.add_argument(
	"dict", 
	action = "store", 
	help = "Filepath to dictionary or URL"
)

parser.add_argument(
	"length", 
	action = "store", 
	default = "5", 
	type = int,
	help = "Length of the words in app dictionary", 
	nargs = "?"
)

args = parser.parse_args()
print(args)

dictionary = []

try: 
	with open(args.dict, "r") as f:
		dictionary = dictFilter(args.length, f.read().split())
except:
	try:
		with urllib.request.urlopen(args.dict) as f:
			dictionary = dictFilter(args.length, f.read().decode('utf-8').split())
	except:
		print(f"Path / URL {args.dict} is not valid")
		exit(0)