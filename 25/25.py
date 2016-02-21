#!/bin/python

a, b, i = (1, 1, 0)

while len(str(b)) < 1000: a, b, i = b, a+b, i+1

print i