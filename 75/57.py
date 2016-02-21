#!/bin/python

def next(cur): return (cur[0]+2*cur[1], cur[0]+cur[1])

count = 0
cur = (1,1)
for i in range(1000):
	if len(str(cur[0])) > len(str(cur[1])): count += 1
	cur = next(cur)
print count