#!/bin/python

primes = open('10.txt')
res = 0
last = 0
while last < 2000000:
	line = primes.readline()
	res += last
	last = int(line)

print "%d" % res