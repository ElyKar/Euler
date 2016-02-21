#!/bin/python
dim = 20
paths = [[0 for i in range(dim+1)] for j in range(dim+1)]

def count(x, y):
	if x == dim and y == dim:
		return 1
	elif paths[x][y] == 0:
		s = 0
		if x < dim:
			s += count(x+1, y)
		if y < dim:
			s += count(x, y+1)
		paths[x][y] = s
		return s
	else:
		return paths[x][y]
		
print "%d" % count(0,0)