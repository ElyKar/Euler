#!/bin/python
res = 0
for a in range(997):
	for b in range(a+1, 997):
		for c in range (b+1, 997):
			if a+b+c == 1000 and a*a+b*b==c*c:
				res = a*b*c

print "%d" % res