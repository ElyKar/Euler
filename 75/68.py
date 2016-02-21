#!/bin/python

#UGLY BRUTE FORCE CODE

from string import join

def isValid(inte, exte):
	if 10 in inte: return False
	D = exte[len(inte)-1]+inte[len(exte)-1]+inte[0]
	for i in range(len(inte)-1):
		if exte[i]+inte[i]+inte[i+1] != D: return False
	return True
	
digits = ['0','1','2','3','4','5','6','7','8','9']
sols = []
perm = set([])

def permute(order):
	if order == len(digits)-1:
		perm.add(join([d for d in digits], ''))
		return
	for i in range(order, len(digits)):
		digits[order], digits[i] = digits[i], digits[order]
		permute(order+1)
		digits[order], digits[i] = digits[i], digits[order]

permute(0)
print len(perm)

def check(x):
	exte = [int(i)+1 for i in x[:5]]
	inte = [int(i)+1 for i in x[5:]]
	if isValid(inte, exte):
		idx = exte.index(min(exte))
		sols.append(toSol((exte*2)[idx:idx+5], (inte*2)[idx:idx+5]))

def toSol(exte, inte):
	sol = ''
	for i in range(len(inte)-1):
		sol += str(exte[i])+str(inte[i])+str(inte[i+1])
	sol += str(exte[len(exte)-1])+str(inte[len(inte)-1])+str(inte[0])
	return int(sol)
	
for s in perm: check(s)
	
print max(sols)