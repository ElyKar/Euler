#!/bin/python

from math import sqrt

squares = [x*x for x in range(1000)]

Ds = [x for x in range(2, 1001) if x not in squares]

maxX = 0
maxD = 0

for D in Ds:
	m = 0
	d = 1
	b0 = int(sqrt(D))
	a = 1
	A = [b0]
	B = [1]
	b = [b0]
	m = d*b0-m
	d = (D-m*m)/d
	b.append((b0+m)/d)
	A.append(b[-1]*b[0]+a)
	B.append(b[-1])
	while A[-1]*A[-1]-D*B[-1]*B[-1] != 1:
		m = d*b[-1]-m
		d = (D-m*m)/d
		b.append((b0+m)/d)
		A.append(b[-1]*A[-1]+a*A[-2])
		B.append(b[-1]*B[-1]+a*B[-2])
	if A[-1] > maxX:
		maxX = A[-1]
		maxD = D
print maxX
print maxD