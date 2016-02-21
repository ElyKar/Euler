#!/bin/python

from math import sqrt
from string import join

count = 0

squares = [x*x for x in range(101)]
irat = [x for x in range(10001) if x not in squares]

for S in irat:
	m = 0
	d = 1
	a0 = int(sqrt(S))
	a = [a0]
	while a[-1] != 2*a0:
		m = d*a[-1]-m
		d = (S-m*m)/d
		a.append((a0+m)/d)
	if (len(a)-1) % 2 == 1: count +=1

print count
