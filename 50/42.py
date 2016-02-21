#!/bin/python

triangles = [n*(n+1)/2 for n in range(1, 1000) if len(str(n)) < len(str(15*26))+1]

convert = {}
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cur = 1
for letter in upper:
	convert[letter] = cur
	cur += 1
	
def count(x, y): return x+y

def value(s):
	count = 0
	global convert
	for letter in s: count += convert[letter]
	return count

f = open('42.txt')
strings = f.read()
strings = strings.rstrip('"').lstrip('"').split('","')


print  reduce(count, [1 for s in strings if value(s) in triangles])