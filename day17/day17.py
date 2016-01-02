#!/usr/bin/python
#title			:day17.py
#description		:advent of code day 17
#author			:Mike Jarrett
#date			:20151231
#version		:1
#usage			:python day17.py
#notes			:
#python_version	:2.6.6
#==============================================================================

import itertools as it
import re

f = open('input.txt')
liters = 150
#f = open('test.txt')
#liters = 25


def read_in(f):
    sizes = []
    for line in f:
        m = re.search('(\d*)',line)
        sizes.append(int(m.group(1)))
        #print line
    return sizes








def subset_sum(numbers, target, partial=[], results=[]):
    s = sum(partial)
    
    # check if the partial sum is equals to target
    if s == target: 
        #print "sum(%s)=%s" % (partial, target)
        results.append(partial)
    if s >= target:
        return   # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n], results ) 
        
    return results
    


sizes = read_in(f)
r = subset_sum(sorted(sizes), liters)
print "part 1: %d" % len(r)

m = min([ len(x) for x in r ])
print m
print [ x for x in r if len(x) == m ]
print "part 2: %d" % len([ x for x in r if len(x) == m ])

