#!/bin/python

def pan(x):
	if '0' in x: return False
	l = [i for i in x]
	return len(set(l)) == 9 and len(l) == 9
	
def dig(x):
	s = ''
	i = 1
	while len(s) < 9:
		s = s + str(i*x)
		i+=1
	return s
	
print max([dig(x) for x in range(100000) if pan(dig(x))])