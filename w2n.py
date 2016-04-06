#!/usr/bin/env python
from number_json import numbers as no
from number_json import signs
li = []

def word2num(word):
	for i in word.split():
		try:
			num = no[i]
			li.append(str(num))
		except:
			sign = signs[i]
			li.append(sign)
	return "".join(li)
# print word2num("ten plus four")