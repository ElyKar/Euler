#!/bin/python

from math import sqrt

def div(x):
	cur = 2
	while cur <= sqrt(x):
		if x%cur == 0: return False
		cur += 1
	return x != 1


primes = [x for x in range(10000) if div(x)]

couples = {}
for p in primes: couples[p] = []

def c(x, y): return div(int(str(x)+str(y))) and div(int(str(y) + str(x)))

for i in range(len(primes)):
	for j in range(i+1, len(primes)):
			if c(primes[i], primes[j]):
					couples[primes[i]].append(primes[j])
					couples[primes[j]].append(primes[i])


triples = {}
for key in couples.keys():
	triples[key] = {}
	for val in couples[key]:
		triples[key][val] = []


for key in couples.keys():
	for i in range(len(couples[key])):
		for j in range(i+1, len(couples[key])):
			if couples[key][i] in couples[couples[key][j]]:
				triples[key][couples[key][i]].append(couples[key][j])
				triples[key][couples[key][j]].append(couples[key][i])
				
quad = {}
for key in triples.keys():
	quad[key] = {}
	for key2 in triples[key].keys():
		quad[key][key2] = {}
		for val in triples[key][key2]:
			quad[key][key2][val] = []

for key in triples.keys():
	for key2 in triples[key].keys():
		for i in range(len(triples[key][key2])):
			for j in range(i+1, len(triples[key][key2])):
				if triples[key][key2][i] in triples[key][triples[key][key2][j]]:
					quad[key][key2][triples[key][key2][i]].append(triples[key][key2][j])
					quad[key][key2][triples[key][key2][j]].append(triples[key][key2][i])


				
quint = {}
for key in quad.keys():
	quint[key] = {}
	for key2 in quad[key].keys():
		quint[key][key2] = {}
		for key3 in quad[key][key2].keys():
			quint[key][key2][key3] = {}
			for val in quad[key][key2][key3]:
				quint[key][key2][key3][val] = []
				
for key in quad.keys():
	for key2 in quad[key].keys():
		for key3 in quad[key][key2].keys():
			for val1 in quad[key][key2][key3]:
				for val2 in quad[key][key2][key3]:
					if val1 in couples[val2]:
						quint[key][key2][key3][val1].append(val2)
						quint[key][key2][key3][val2].append(val1)

for key in quint.keys():
	for key2 in quint[key].keys():
		for key3 in quint[key][key2].keys():
			for key4 in quint[key][key2][key3]:
				for val in quint[key][key2][key3][key4]:
					print "%s, %s, %s, %s, %s" % (key, key2, key3, key4, val)