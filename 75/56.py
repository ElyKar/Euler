#!/bin/python

def add(x): return sum([int(l) for l in str(x)])

print max([add(a**b) for a in range(100) for b in range(100)])