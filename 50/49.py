#!/bin/python

from math import sqrt

def div(x):
	cur = 2
	while cur <= sqrt(x):
		if x%cur == 0: return False
		cur += 1
	return x != 1

def isPerm(i, j):
	x, y = str(i), str(j)
	if len(x) != len(y): return False
	for letter in x:
		if x.count(letter) != y.count(letter): return False
	return True
	
for cur in range(1000, 10000-6660):
	flag = True
	for i in range(3):
		flag = flag and div(cur+i*3330) and isPerm(cur, cur+i*3330)
	if flag:
		print cur
		print cur+3330
		print cur+6660
		print ''
