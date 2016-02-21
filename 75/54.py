#!/bin/python

from string import join

values = ['2','3','4','5','6','7','8','9','A','B','C','D','E']
reverse = {}
cur = 1
hashfunc = {}
hashfunc['Pair'] = 1
hashfunc['Pairs'] = 2
hashfunc['Three'] = 3
hashfunc['Straight'] = 4
hashfunc['Flush'] = 5
hashfunc['Full'] = 6
hashfunc['Four'] = 7
hashfunc['straightFlush'] = 8
hashfunc['royalFlush'] = 9
step = 10000000

for v in values:
	reverse[v] = cur
	cur += 1

def royalFlush(hand):
	color = hand[0][1]
	if 'T'+color in hand and 'J'+color in hand and 'Q'+color in hand and 'K'+color in hand and 'A'+color in hand:
		return step**hashfunc['royalFlush']+High(hand)
	return 0
	
def straightFlush(hand):
	color = hand[0][1]
	cards = [v+color for v in values]
	if join(hand) in join(cards):
		return step**hashfunc['straightFlush']+High(hand)
	return 0
	
def Four(hand):
	l = [card[0] for card in hand]
	if len(set(l)) == 2 and (l.count(l[0]) == 1 or l.count(l[0]) == 4):
		card = '0'
		for c in l:
			if l.count(c) == 4: card = c
		return (step**hashfunc['Four'])*reverse[card]+High(removeVal(hand, card))
	return 0
	
def Full(hand):
	l = [card[0] for card in hand]
	if len(set(l)) == 2 and (l.count(l[0]) == 2 or l.count(l[0]) == 3):
		card = '0'
		for c in l:
			if l.count(c) == 3: card = c
		return (step**hashfunc['Full'])*reverse[card]+High(removeVal(hand, card))
	return 0
	
def Straight(hand):
	vals = [card[0] for card in hand]
	if join(vals) in join(values):
		return step**hashfunc['Straight']+High(hand)
	return 0
	
def Flush(hand):
	if len(set([card[1] for card in hand])) == 1:
		return step**hashfunc['Flush']+High(hand)
	return 0
	
def Three(hand):
	l = [card[0] for card in hand]
	count = step**hashfunc['Three']
	card = '1'
	for c in l:
		if l.count(c) == 3: card = c
	if card == '1':
		return 0
	return count*reverse[card]+High(removeVal(hand, card))
	
def Pairs(hand):
	l = [card[0] for card in hand]
	c = step**hashfunc['Pairs']
	paircard = '1'
	pairs  = 0
	for card in l:
		if l.count(card) == 2:
			pairs += 1
		if l.count(card) == 2 and (paircard == '1' or reverse[card] > reverse[paircard]): paircard = card
	if paircard == '1' or pairs != 4:
		return 0
	return c*reverse[paircard]+Pair(removeVal(hand, paircard))
	
def Pair(hand):
	l = [card[0] for card in hand]
	c = step**hashfunc['Pair']
	paircard = '1'
	for card in l:
		if l.count(card) == 2: paircard = card
	if paircard == '1':
		return 0
	return c*reverse[paircard]+High(removeVal(hand, paircard))
	
def High(hand):
	cur = 0
	l = [card[0] for card in hand]
	while len(l) > 0:
		maxcard = '2'
		for card in l:
			if reverse[card] > reverse[maxcard]: maxcard = card
		cur = cur*16 + reverse[maxcard]
		l.remove(maxcard)
	return cur

def removeVal(hand, val): return [x for x in hand if x[0] != val]

def removeCol(hand, col): return [x for x in hand if x[1] != col]

def hashCode(hand):
	return max([High(hand), Pair(hand), Pairs(hand), Three(hand), Straight(hand), Flush(hand), Full(hand), Four(hand), straightFlush(hand), royalFlush(hand)])


hands = open('54.txt','r')
count1 = 0
for h in hands:
	hand = h.replace('A','E').replace('T','A').replace('J','B').replace('Q','C').replace('K','D').split()
	if hashCode([card for card in sorted(hand[:5])]) > hashCode([card for card in sorted(hand[5:])]): count1 += 1
	
print count1