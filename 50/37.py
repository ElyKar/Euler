#!/bin/python

from math import sqrt

def div(x):
	cur = 2
	while cur <= sqrt(x):
		if x%cur == 0: return False
		cur += 1
	return x != 1

def trunc(x):
	s = str(x)
	for i in range(1,len(s)):
		if not div(int(s[0:i])) or not div(int(s[i:len(s)])): return False
	return div(x)
	
print sum([x for x in range(10, 1000000) if trunc(x)])