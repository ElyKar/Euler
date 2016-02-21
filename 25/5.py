#!/bin/python
cur = 0
flag = False
while not flag:
	flag = True
	cur = cur+20
	for i in range(2, 21):
		flag = flag and cur%i==0
	print "%d" % cur

print "%d" % cur