#!/usr/bin/python

"""
created by Mike Jarrett
"""

import re

f = open('input.txt','r')
text = f.read()

steps = re.findall(r'(\D)', text)

steps = [ w.replace('(', '1') for w in steps ]
steps = [ w.replace(')', '-1') for w in steps ]
del steps[-1]

steps = [ int(w) for w in steps ]

floor = 0
count = 0

for step in steps:
    floor += step
    count += 1
    if floor < 0:
        print count
        break


#print steps
