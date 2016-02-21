#!/bin/python
maxchain = 0
maxn = 0
for i in range(1, 1000001):
	x = i
	count = 0
	while x != 1:
		if x % 2 == 0:
			x = x/2
		else:
			x = 3*x+1
		count += 1
	print "%d" % i
	if count > maxchain:
		maxchain = count
		maxn = i

print "%d" % maxn