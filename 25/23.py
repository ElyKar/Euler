#!/bin/python
def div(x):
	divs = [1]
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
	
def add(x, y): return x+y
	
abundant = [i for i in range(1,28124) if div(i) > i]
s = set([x+y for x in abundant for y in abundant if x+y < 28124])
count = reduce(add, [i for i in range(1, 28124) if i not in s])
print count