#!/bin/python
maxi = 0
for x in range(100, 1000):
	for y in range(100, 1000):
		z = x*y
		if int(("%d" % z)[::-1]) == z:
			maxi = max(maxi, z)

print "%d" % maxi