#!/bin/python

top = 100

part = [[0 for i in range(top+1)] for i in range(top+1)]
for i in range(top):
	part[i+1][1] = 1
	part[i+1][i+1] = 1
	
def p(n, k):
	if n < k: return 0
	if part[n][k] != 0: return part[n][k]
	part[n][k] = p(n-1, k-1) + p(n-k, k)
	return part[n][k]

print sum([p(top, i) for i in range(1, top+1)])