#!/usr/bin/env python3

import argparse
import sys
import urllib.request
import random

dictionary = []

def dictFilter(l, lst):
	return list(filter(lambda x: len(x) == l, lst))

def chooseRandomWord(lst):
	return lst[random.randint(0, len(lst))]

parser = argparse.ArgumentParser(
	prog = "Bulls and cows",
	description = "03 task",
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

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
	secret = chooseRandomWord(words)
	guess = ''
	cnt_ask = 0
	while guess != secret:
#		ask()
		cnt_ask += 1
#		bullscows()
#		inform()
		break # tmp
	return cnt_ask

args = parser.parse_args()
print(args)

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
		