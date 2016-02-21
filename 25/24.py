#!/bin/python

digits = ['0','1','2']#,'3','4','5','6','7','8','9']

fact = 1
facto = []
for i in range(1,4):
	facto.append(fact*i)
	fact = fact*i
facto = [i for i in reversed(facto)]
print facto
cur = 0
mark = 1
res = ''
while cur < 3:
	print res
	idx = mark/facto[cur]
	mark = mark%facto[cur]
	res = res+digits[idx]
	digits.remove(digits[idx])
	cur += 1
print res