#!/bin/python

from string import join

def Pal(x): return int(join([letter for letter in reversed(str(x))], ''))

def isPal(x): return str(x) == str(Pal(x))

def isLychrel(x):
	y = x
	count = 1
	while count < 51:
		y = y + Pal(y)
		if isPal(y): return False
		count += 1
	return True
	
print isLychrel(1)

print sum([1 for x in range(2, 10001) if isLychrel(x)])
		