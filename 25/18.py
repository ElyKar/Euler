#!/bin/python

pyramid = []
pyramid.append('75'.split(' '))
pyramid.append('95 64'.split(' '))
pyramid.append('17 47 82'.split(' '))
pyramid.append('18 35 87 10'.split(' '))
pyramid.append('20 04 82 47 65'.split(' '))
pyramid.append('19 01 23 75 03 34'.split(' '))
pyramid.append('88 02 77 73 07 63 67'.split(' '))
pyramid.append('99 65 04 28 06 16 70 92'.split(' '))
pyramid.append('41 41 26 56 83 40 80 70 33'.split(' '))
pyramid.append('41 48 72 33 47 32 37 16 94 29'.split(' '))
pyramid.append('53 71 44 65 25 43 91 52 97 51 14'.split(' '))
pyramid.append('70 11 33 28 77 73 17 78 39 68 17 57'.split(' '))
pyramid.append('91 71 52 38 17 14 91 43 58 50 27 29 48'.split(' '))
pyramid.append('63 66 04 68 89 53 67 30 73 16 69 87 40 31'.split(' '))
pyramid.append('04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'.split(' '))
copy = [[0 for x in range(y+1)] for y in range(len(pyramid))]

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