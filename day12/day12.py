#!/usr/bin/python
#title			:day12.py
#description		:advent of code day 12
#author			:Mike Jarrett
#date			:20151229
#version		:1
#usage			:python day12.py
#notes			:
#python_version	:2.6.6
#==============================================================================
import re
import json
from pprint import pprint

f = open('input.txt')
text = f.read()
f.close()

digits = re.findall('-?\d+',text)

#print digits
print "Part 1: " + str(sum([int(n) for n in digits]))


        
def Flatten(obj):
    if type(obj) in [str, unicode]:
        return 0
    if type(obj) in [int, float]:
        return obj
    if type(obj) is dict:
        if 'red' in obj.values(): return 0
        obj = obj.values()
    if type(obj) is list:
        return sum(map(Flatten, obj))
    raise ValueError(type(obj))

print Flatten(json.loads(open('input.txt').read()))
