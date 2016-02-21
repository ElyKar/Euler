#!/bin/python

from math import sqrt

def div(x):
	cur = 2
	while cur <= sqrt(x):
		if x%cur == 0: return False
		cur += 1
	return True

def cycle(x):
	s = str(x)
	for i in range(len(s)):
		if not div(int(s)): return False
		s = s.replace(s[0],'',1)+s[0]
	return True

print sum([1 for x in range(2, 1000000) if cycle(x)])
