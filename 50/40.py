#!/bin/python

irat = ''
i = 1
while len(irat) < 1000000:
	irat += str(i)
	i+=1
	
print int(irat[0])*int(irat[9])*int(irat[99])*int(irat[999])*int(irat[9999])*int(irat[99999])*int(irat[999999])