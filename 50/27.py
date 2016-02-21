#!/bin/python
import math
def div(x):
	if x < 0: return False
	cur = 2
	while cur < math.sqrt(x):
		if x%cur == 0: return False
		cur += 1
	return True
	
def longest(a, b):
	cur = 0
	flag = True
	while flag:
		flag = div(formula(a, b, cur)) == 1
		cur+=1
	return cur
def formula(a, b, n): return n*n+a*n+b
maxi = 0
maxab = (0,0)
for a in range(-999, 999):
	print a
	for b in range(-999, 999):
		if div(formula(a, b, maxi+1)) and longest(a, b) > maxi:
			maxi = longest(a, b)
			print maxi
			maxab = (a, b)
print "%d : %d" % maxab
print "%d" % (maxab[0]*maxab[1])