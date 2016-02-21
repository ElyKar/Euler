#!/bin/python
primes = []
primes.append(2)
for i in range(3, 1000001, 2):
	primes.append(i)
print "done"
for i in primes:
	for j in primes:
		if i!=j and j%i== 0:
			primes.remove(j)
	#if i%1000==0:
	print "%d" % i


print "%d" % primes[10000]