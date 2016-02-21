#!/bin/python

def pal(x): return list(x) == [i for i in reversed(x)]
print sum([x for x in range(1000000) if pal(str(x)) and pal("{0:b}".format(x))])