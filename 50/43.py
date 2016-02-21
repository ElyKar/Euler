#!/bin/python

from string import join

digits = ['0','1','2','3','4','5','6','7','8','9']
current =  []
perm = set([])
count = 0

def add(x, y): return x+y

def permute(order):
	global count
	if order == len(digits)-1:
		count +=1
		perm.add(join([d for d in digits], ''))
		return
	for i in range(order, len(digits)):
		digits[order], digits[i] = digits[i], digits[order]
		permute(order+1)
		digits[order], digits[i] = digits[i], digits[order]

permute(0)

def check(x):
	return int(x[1:4])%2==0 and int(x[2:5])%3==0 and int(x[3:6])%5==0 and int(x[4:7])%7==0 and int(x[5:8])%11==0 and int(x[6:9])%13==0 and int(x[7:10])%17==0

print check('1406357289')

print sum([int(x) for x in perm if check(x)])
print count