#!/bin/python

def isPerm(i, j):
	x, y = str(i), str(j)
	if len(x) != len(y): return False
	for letter in x:
		if x.count(letter) != y.count(letter): return False
	return True
	
def check(x):
	return isPerm(x, 2*x) and isPerm(x, 3*x) and isPerm(x, 4*x) and isPerm(x, 5*x) and isPerm(x, 6*x)
	
for i in range(100000000):
	if check(i): print i
