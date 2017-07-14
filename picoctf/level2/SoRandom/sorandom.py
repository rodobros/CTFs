#!/usr/bin/python -u
import random,string

def recoverSeed(passwordNow) :
	encflag = ""
	random.seed("random")
	for c in passwordNow:
		if c.islower():
			encflag += chr((ord(c)-ord('a')+random.randrange(0,26))%26 + ord('a'))
		elif c.isupper():
			encflag += chr((ord(c)-ord('A')+random.randrange(0,26))%26 + ord('A'))
		elif c.isdigit():
			encflag += chr((ord(c)-ord('0')+random.randrange(0,10))%10 + ord('0'))
		else:
			encflag += c


coolflag = ""
random.seed("random")
for c in "BNZQ:1l36de9583w5516fv3b8691102224f3e":
	for i in range(48, 122 + 1):
		encchar = ''
		if chr(i).islower():
			encchar = chr((i-ord('a')+random.randrange(0,26))%26 + ord('a'))
		elif chr(i).isupper():
			encchar = chr((i-ord('A')+random.randrange(0,26))%26 + ord('A'))
		elif chr(i).isdigit():
			encchar = chr((i-ord('0')+random.randrange(0,10))%10 + ord('0'))
		else:
			encchar = chr(i)
		if encchar == c:
			coolflag += chr(i)
			break
		else:
			recoverSeed(coolflag)
print coolflag