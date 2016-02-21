#!/bin/python

f = open('67.txt', 'r')

pyramid = [[int(x) for x in line.split()] for line in f]
copy = [[0 for i in range(L)] for L in range(1, 101)]

X = len(pyramid)-1

def init(x, y):
	global pyramid
	global copy
	global X
	
	if x == X:
		copy[x][y] = int(pyramid[x][y])
	elif copy[x][y] != 0:
		return
	else:
		init(x+1, y)
		init(x+1, y+1)
		copy[x][y] = int(pyramid[x][y]) + max(copy[x+1][y],copy[x+1][y+1])

init(0,0)

print "%d" % copy[0][0]