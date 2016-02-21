#!/bin/python

from decimal import *
import re
maxi = 0
maxidx = 0

def longest(s):
	cur = 0
	sub = ''
	for start in range(len(s)):
		end = start+1
		test = s[start]
		while end < len(s) and len(sub) == 0:
			if test == s[end:end+end-start]:
				sub = test
			test += s[end]
			end += 1
	return len(sub)
			
	
getcontext().prec = 10000
#frac = str(Decimal(1)/Decimal(2)).replace('0.','').rstrip('0').lstrip('0')
#print longest(frac)
for d in range(2,1000):
	frac = str(Decimal(1)/Decimal(d)).replace('0.','').rstrip('0').lstrip('0')
	count = longest(frac)
	if count > maxi:
		maxi = count
		maxidx = d
	print '%d : %d' % (d, maxi)
print maxidx