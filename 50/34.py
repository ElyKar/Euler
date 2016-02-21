#!/bin/python

def fact(n):
	if n == 1 or n == 0: return 1
	return n*fact(n-1)

facto = [fact(i) for i in range(10)]
def fact(x): return sum([facto[int(i)] for i in str(x)])
res = [x for x in range(10,10000000) if fact(x) == x]
print sum(res)