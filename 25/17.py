#!/bin/python
units = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
hundred = 'hundred'
a = 'and'
thousand = 'thousand'

sletter = 0
for i in range(1, 1000):
	x = i
	chain = ''
	chain += units[x/100]
	if x/100 > 0:
		chain += hundred
		if x%100 != 0:
			chain += a
	x = x%100
	if x < 20:
		chain += units[x]
	else:
		chain += tens[x/10]+units[x%10]
	sletter += len(chain)
	print chain

sletter += len('onethousand')

print "%d" % sletter