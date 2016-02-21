#!/bin/python

N = 10000

penta = set([n*(3*n-1)/2 for n in range(1, N)])

print min([abs(x-y) for x in penta for y in penta if x+y in penta and x-y in penta])