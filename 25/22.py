#!/bin/python

f = open('22.txt')
line = f.readline()
f.close()
names = line.replace('\"','').replace('\n','').split(',')
names.sort()
pos = 1
s = 0
for name in names:
	score = 0
	for letter in name:
		score += ord(letter)-ord("A")+1
	s += pos*score
	pos += 1

print "%d" % s