#!/bin/python

from string import join

f = open('59.txt', 'r')
cipher = [int(x) for x in f.read().rstrip('\n').split(',')]
f.close()

letters = 'abcdefghijklmnopqrstuvwxyz'
the = 'world'

possibilities = []

for a in range(26):
	for b in range(26):
		for c in range(26):
			k = letters[a]+letters[b]+letters[c]
			key = [ord(letter) for letter in k*400+k[0]]
			decrypt = join([chr(cipher[i] ^ key[i]) for i in range(len(cipher))], '')
			if the in decrypt: possibilities.append(k)

for k in possibilities:
	key = [ord(letter) for letter in k*400+k[0]]
	print ("NEW POSSIBILITY : %s" % k)
	print join([chr(cipher[i] ^ key[i]) for i in range(len(cipher))], '')
	
k = 'god'
key = [ord(letter) for letter in k*400+k[0]]

print sum([cipher[i] ^ key[i] for i in range(len(cipher))])