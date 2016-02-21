#!/bin/python
power = 2**1000
s = 0
for char in "%s" % power:
	s += int(char)
print "%d" % s