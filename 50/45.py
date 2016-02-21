#!/bin/python

tri = set([n*(n+1)/2 for n in range(100000)])
penta = set([n*(3*n-1)/2 for n in range(100000)])
hexa = set([n*(2*n-1) for n in range(100000)])

for n in hexa:
	if n in penta and n in tri:
		print n