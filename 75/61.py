#!/bin/python

def fil(x): return len(str(x)) == 4

def check(n, numbers):
	for num in numbers:
		if str(n)[:2] == str(num)[-2:]: return True
	return False
	
def sure(x, y):return str(x)[-2:] == str(y)[2:]

triangle = set([n*(n+1)/2 for n in range(10000) if fil(n*(n+1)/2)])
square = set([n*n for n in range(10000) if fil(n*n)])
penta = set([n*(3*n-1)/2 for n in range(10000) if fil(n*(3*n-1)/2)])
hexa = set([n*(2*n-1) for n in range(10000) if fil(n*(2*n-1))])
hepta = set([n*(5*n-3)/2 for n in range(10000) if fil(n*(5*n-3)/2)])
octa = set([n*(3*n-2) for n in range(10000) if fil(n*(3*n-2))])
triangle = set([x for x in triangle if fil(x) and x not in hexa])

sets = [triangle, square, penta, hexa, hepta, octa]
for i in range(len(sets)):
	for j in range(len(sets)):
		if not i==j:
			for k in range(len(sets)):
				if not k==j and not k==i:
					for l in range(len(sets)):
						if not l==k and not l==j and not l==i:
							for m in range(len(sets)):
								if not m==l and not m==k and not m==j and not m==i:
									for n in range(len(sets)):
										if not n==m and not n==l and not n==k and not n==j and not n==i:
											cache = 0
											ref = [[x for x in cur] for cur in sets]
											while len(ref[i])+len(ref[j])+len(ref[k])+len(ref[m])+len(ref[n])+len(ref[l]) != cache:
												cache = len(ref[i])+len(ref[j])+len(ref[k])+len(ref[m])+len(ref[n])+len(ref[l])
												ref[i] = set([x for x in ref[i] if check(x, ref[n])])
												ref[j] = set([x for x in ref[j] if check(x, ref[i])])
												ref[k] = set([x for x in ref[k] if check(x, ref[j])])
												ref[l] = set([x for x in ref[l] if check(x, ref[k])])
												ref[m] = set([x for x in ref[m] if check(x, ref[l])])
												ref[n] = set([x for x in ref[n] if check(x, ref[m])])
											if cache != 0:
												print "%s, %s" % (cache, ref)
