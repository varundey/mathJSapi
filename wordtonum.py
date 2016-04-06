"""
	This module is to convert words to standard number representation


"""
#!/usr/bin/env python
import re

class WordsToNumbers():
    __ones__ = { 'one':   1, 'eleven':     11,
                 'two':   2, 'twelve':     12,
                 'three': 3, 'thirteen':   13,
                 'four':  4, 'fourteen':   14,
                 'five':  5, 'fifteen':    15,
                 'six':   6, 'sixteen':    16,
                 'seven': 7, 'seventeen':  17,
                 'eight': 8, 'eighteen':   18,
                 'nine':  9, 'nineteen':   19 }
    __tens__ = { 'ten':     10,
                 'twenty':  20,
                 'thirty':  30,
                 'forty':   40,
                 'fifty':   50,
                 'sixty':   60,
                 'seventy': 70,
                 'eighty':  80,
                 'ninety':  90 }
    __groups__ = { 'thousand':  1000,
		   'lakh':100000,
		   'crore':10000000,
                   'million':   1000000,
                   'billion':   1000000000,
                   'trillion':  1000000000000 }
    

    
    __groups_re__ = re.compile(
        r'\s?([\w\s]+?)(?:\s((?:%s))|$)' %
        ('|'.join(__groups__))
        )
    __hundreds_re__ = re.compile(r'([\w\s]+)\shundred(?:\s(.*)|$)')
    __tens_and_ones_re__ =  re.compile(
        r'((?:%s))(?:\s(.*)|$)' %
        ('|'.join(__tens__.keys()))
        )


    def parse(self, words):
        words = words.lower()
        groups = {}        
        num = 0
        for group in WordsToNumbers.__groups_re__.findall(words):
            group_multiplier = 1
            if group[1] in WordsToNumbers.__groups__:
                group_multiplier = WordsToNumbers.__groups__[group[1]]
            group_num = 0
            hundreds_match = WordsToNumbers.__hundreds_re__.match(group[0])
            tens_and_ones = None
            if hundreds_match is not None and hundreds_match.group(1) is not None:
                group_num = group_num + \
                            (WordsToNumbers.__ones__[hundreds_match.group(1)] * 100)
                tens_and_ones = hundreds_match.group(2)
            else:
                tens_and_ones = group[0]
            if tens_and_ones is None:
                num = num + (group_num * group_multiplier)
                continue
            tn1_match = WordsToNumbers.__tens_and_ones_re__.match(tens_and_ones)
            if tn1_match is not None:
                group_num = group_num + WordsToNumbers.__tens__[tn1_match.group(1)]
                if tn1_match.group(2) is not None:
                    group_num = group_num + WordsToNumbers.__ones__[tn1_match.group(2)]
            else:
                group_num = group_num + WordsToNumbers.__ones__[tens_and_ones]
            num = num + (group_num * group_multiplier)
        return num

w2n =  WordsToNumbers()
#print w2n.parse("forty two")