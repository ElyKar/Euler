#!/bin/python3.4

f = open('82.txt', 'r')

mtx = [[131,673,234,103,18],
	[201,96,352,965,150],
	[630,803,746,422,111],
	[537,699,497,121,956],
	[805,732,524,37,331]]
#for line in f:
#	mtx.append([int(x) for x in line.split(',')])
	
def curMin(i, j, f):
	if i >= len(mtx) or i < 0: return float('inf')
	if copy[i][j] != -1: return copy[i][j]
	if f == 0:
		copy[i][j] = mtx[i][j]+min(curMin(i, j+1, 1), curMin(i+1, j, 0))
		print("Min between %f and %f is %f" % (curMin(i, j+1, 1), curMin(i+1, j, 0), min(curMin(i, j+1, 1), curMin(i+1, j, 0))))
	elif f == 1:
		copy[i][j] = mtx[i][j]+min(curMin(i-1, j, 2), curMin(i, j+1, 1), curMin(i+1, j, 0))
		print("Min between %f, %f and %f is %f" % (curMin(i-1, j, 2), curMin(i, j+1, 1), curMin(i+1, j, 0), min(curMin(i-1, j, 2), curMin(i, j+1, 1), curMin(i+1, j, 0))))
	else:
		copy[i][j] = mtx[i][j]+min(curMin(i, j+1, 1), curMin(i-1, j, 2))
		print("Min between %f and %f is %f" % (curMin(i, j+1, 1), curMin(i-1, j, 2), min(curMin(i, j+1, 1), curMin(i-1, j, 2))))
	return copy[i][j]
	
curM = 1000000000
for i in range(5):
	copy = [[-1 for i in range(5)] for j in range(5)]
	for i in range(len(copy)): copy[i][len(copy)-1] = mtx[i][len(copy)-1]
	lastM = curMin(i, 0, 1)
	if curM > lastM: curM = lastM
	print(lastM)
	for x in copy: print(x)
print(curM)