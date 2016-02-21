#!/bin/python

count = 0

for i in range(1, 100):
	cur = 1
	while len(str(cur**i)) <= i:
		if len(str(cur**i)) == i:
			print "%s ; %s : %s" % (cur, i, cur**i)
			count +=1
		cur += 1
		
print count