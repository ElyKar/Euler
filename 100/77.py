#!/bin/python3.4

from math import sqrt

class Poly:
	def __init__(self, order):
		self.rank = order
		self.polyn = [0 for i in range(order)]
		
	def setP(self, array):
		self.polyn = array
	
	def add(self, p):
		self.polyn = [self.polyn[i] + p.polyn[i] for i in range(self.rank)]
	
	def mul(self, p):
		q = Poly(self.rank)
		t = Poly(self.rank)
		for i in range(self.rank):
			q.polyn = [0 for k in range(i)]+[p.polyn[k]*self.polyn[i] for k in range(self.rank)]
			t.add(q)
		self.polyn = t.polyn
	
	def __str__(self):
		res = ''
		for i in range(self.rank):
			res += '%sX**%s  ' % (self.polyn[i], i)
		return res
		
	def get(self, order):
		return  self.polyn[order]
		
def div(x):
	cur = 2
	while cur <= sqrt(x):
		if x%cur == 0: return False
		cur += 1
	return x != 1

primes = [x for x in range(1,1000) if div(x)]

curP = 0
cur = 2
curPoly = Poly(1000)
curPoly.setP([1]+[0]*999)
while True:
	if primes[curP] <= cur:
		p = Poly(1000)
		ar = ([1]+[0 for i in range(primes[curP]-1)])*int((1000/primes[curP]+1))
		p.setP(ar)
		curPoly.mul(p)
		curP += 1
	if curPoly.get(cur) > 5000:
		print(cur)
		break
	cur +=1
	