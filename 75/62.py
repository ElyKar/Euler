#!/bin/python

import time

start = time.time()

def isPerm(i, j):
	x, y = str(i), str(j)
	#if len(x) != len(y): return False
	for letter in x:
		if x.count(letter) != y.count(letter): return False
	return True
	
cubes = [[] for i in range(25)]
for i in range(100000):
	cubes[len(str(i*i*i))].append(i*i*i)
	
print "Init"
	
for array in cubes:
	for cube in array:
		count = 0
		for c in array:
			if isPerm(c, cube): count += 1
		if count == 5:
			print cube
			print time.time()-start