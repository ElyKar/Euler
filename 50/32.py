#!/bin/python

def evalue(n): 
	l = [x for x in str(n)]
	return len(set(l)) == len(l)
	
def evaluate(x, y, z):
	l = [x for x in str(x)+str(y)+str(z)]
	return len(set(l)) == 9 and len(l) == 9

s = set()
for x in range(10000):
	if '0' not in str(x) and evalue(x):
		for y in range(10000):
			if '0' not in str(y) and '0' not in str(x*y) and evalue(y) and evaluate(x, y, x*y):
				s.add(x*y)
		print x
print sum(s)