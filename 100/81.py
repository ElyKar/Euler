#!/bin/python3.4

f = open('81.txt', 'r')
mtx = [[float('inf') for i in range(82)]]

for line in f:
	mtx.append([float('inf')]+[int(x) for x in line.split(',')]+[float('inf')])
mtx.append([float('inf') for i in range(82)])
	
for i in range(1, len(mtx)-1):
	for j in range(1, len(mtx)-1):
		if i!=1 or j!= 1:
			mtx[i][j] = mtx[i][j] + min(mtx[i-1][j], mtx[i][j-1])
			
print(mtx[len(mtx)-2][len(mtx)-2])