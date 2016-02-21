#!/bin/python3.4

from decimal import *
from math import sqrt

getcontext().prec = 102

def red(x):
	print(len(str(x).replace('.', '')))
	return str(x).replace('.', '')[:100]

decs = [Decimal(i).sqrt() for i in range(1, 101) if i != int(sqrt(i))*int(sqrt(i))]
print(sum([sum([int(x) for x in s]) for s in map(red, decs)]))
print(len(decs))
print(sum([int(x) for x in red(decs[0])]))
