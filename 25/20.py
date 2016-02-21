#!/bin/python
fact = 1
for i in range(1, 101):
	fact *= i
print "%d" % fact
count = 0
for digit in "%s" % fact:
	count += int(digit)

print "%d" % count