#!/bin/python

months = [31,28,31,30,31,30,31,31,30,31,30,31]

cur = 0
count = 0
for i in range(3, len(months)):
	cur += months[i]

for year in range(1901, 1902):
	for month in months:
		cur += month
		if month == 28 and year%4 == 0:
			cur += 1
		if cur%7 == 0:
			count += 1
			cur = 0

print "%d" % count