#!/bin/python
first = 600851475143
maxi = 0
cur = 2
while cur <= first :
	if first%cur==0:
		maxi = max(cur, maxi)
		first = first/cur
		cur = 2
	else :
		cur += 1

print "%d" % maxi