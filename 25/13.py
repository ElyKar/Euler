#!/bin/python
f = open("13.txt","r")
s = 0
for line in f:
	s = s + int(line)

print "%d" % s