#!/bin/python

def factor(n):
	if n == 1: return 1
	return n*factor(n-1)
	
def comb(n, r):
	return fact[n]/(fact[r]*fact[n-r])
	
fact = [1]
for i in range(1, 101): fact.append(factor(i))

print comb(23, 10)

print sum([1 for n in range(1, 101) for r in range(1, n+1) if comb(n, r) > 1000000])