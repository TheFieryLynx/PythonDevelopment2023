#!/usr/bin/env python3

import argparse
import sys
import urllib.request
import random

from io import StringIO
import cowsay

cow = cowsay.get_random_cow()

dictionary = []

def dictFilter(l, lst):
	return list(filter(lambda x: len(x) == l, lst))

def chooseRandomWord(lst):
	return lst[random.randint(0, len(lst) - 1)]

def custom_cowprint(msg):
	print(cowsay.cowsay(
		msg.strip(),
		cow=cow
	))

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
	custom_cowprint(prompt)
	if valid == None:
		inp = input()
		while len(inp) != args.length:
			custom_cowprint(prompt)
			inp = input()
	else:
		inp = input()
		while inp not in valid:
			custom_cowprint(prompt)
			inp = input()
	return inp

def inform(format_string: str, bulls: int, cows: int) -> None:
	custom_cowprint(format_string.format(bulls, cows))
	
def bullscows(guess: str, secret: str) -> (int, int):
	bulls, cows = 0, 0
	bulls_positions = [0 for i in range(len(guess))]
	for i in range(len(guess)):
		if guess[i] == secret[i]:
			bulls += 1
			bulls_positions[i] = 1
	for i in range(len(guess)):
		if guess[i] != secret[i]:
			for j in range(len(bulls_positions)):
				if bulls_positions[j] != 1 and guess[i] == secret[j]:
					cows += 1
					bulls_positions[j] = 1
	return bulls, cows

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
	secret = chooseRandomWord(words)
	guess = ''
	cnt_ask = 0
	while guess != secret:
		guess = ask("Введите слово: ") # ask("Введите слово: ", words) - more interesting with random words :)
		cnt_ask += 1
		bulls, cows = bullscows(guess, secret)
		inform("Быки: {}, Коровы: {}", bulls, cows)
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