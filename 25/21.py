#!/bin/python

def div(x):
	divs = [1]
	if x == 1:
		return 1
	first = 1
	last = x
	while last - first > 1:
		first += 1
		if x%first == 0:
			divs.append(first)
			if first != x/first:
				divs.append(x/first)
			last = x/first
	s = 0
	for i in divs: s += i
	return s

count = 0

for x in range(1, 10001):
	y = div(x)
	if x != y and div(y) == x:
		count += x + y
print "%d" % (count/2)