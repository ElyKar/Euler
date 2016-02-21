#!/bin/python

u = [2, 3]
fact = 2
while len(u) != 100:
	if (len(u)+1) % 3 == 0:
		u.append(fact*u[-1]+u[-2])
		fact += 2
	else:
		u.append(u[-1]+u[-2])
print u
print sum([int(x) for x in str(u[-1])])