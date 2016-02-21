#!/bin/python

coins = [100, 50, 20, 10, 5, 2, 1]
count = 0
s = set([])
processed = set([])

def value(position):
	global coins
	return sum(position[i]*coins[i] for i in range(len(position)))
	
def hashed(position):
	return sum([position[i]*201**i for i in range(len(position))])
	
def compute(position):
	v = value(position)
	if v > 200: return
	if v == 200:
		global s
		s.add(hashed(position))
		return
	for i in range(len(position)):
		global count
		count += 1
		if count%10000 == 0: print count
		position[i] += 1
		if (hashed(position) not in processed):
			processed.add(hashed(position))
			compute(position)
		position[i] -= 1

compute([0,0,0,0,0,0,0])

s.add(-1) # One coin of 2 pounds is also a solution

print "%s" % len(s)