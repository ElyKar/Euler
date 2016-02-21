#!/bin/python3.4

penta = [int(k*(3*k-1)/2) for k in range(1,100000)]
part = [1]

s = 1
n = 0

curR = 0
remove = False
while s%1000000 != 0:
	n += 1
	s = 0
	curK = 0
	while penta[curK] <= n:
		if curK%2 == 0:
			s += part[n-penta[curK]]
			if penta[curK]+curK+1 <= n:
				s += part[n-(penta[curK]+curK+1)]
		else:
			s -= part[n-penta[curK]]
			if penta[curK]+curK+1 <= n:
				s -= part[n-(penta[curK]+curK+1)]
		curK += 1
	part.append(s)
	print(s, n)
print(s)