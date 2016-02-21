#!/bin/python

def fifth(x): return sum([int(l)**5 for l in str(x)])

numbers = [x for x in range(2, 1000000) if x == fifth(x)]

print "%d" % sum(numbers)