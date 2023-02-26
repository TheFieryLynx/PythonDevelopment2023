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

args = parser.parse_args()

def ask(prompt: str, valid: list[str] = None) -> str:
	print(prompt)
	if valid == None:
		inp = input()
		while len(inp) != args.length:
			print(prompt)
			inp = input()
	else:
		inp = input()
		while inp not in valid:
			print(prompt)
			inp = input()
	return inp

def inform(format_string: str, bulls: int, cows: int) -> None:
	None
	
def bullscows(guess: str, secret: str) -> (int, int):
	bulls, cows = 0, 0
	for i in range(len(guess)):
		if guess[i] == secret[i]:
			bulls += 1
		else:
			if guess[i] in secret:
				cows += 1
	return bulls, cows

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
	secret = chooseRandomWord(words)
	guess = ''
	cnt_ask = 0
	while guess != secret:
		guess = ask("Введите слово: ") # ask("Введите слово: ", words) - more interesting with random words :)
		cnt_ask += 1
		bulls, cows = bullscows(guess, secret)
#		inform()
		break # tmp
	return cnt_ask

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
		
print(gameplay(ask, inform, dictionary))