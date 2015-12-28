#!/usr/bin/python
#title			:day8.py
#description		:advent of code day 8
#author			:Mike Jarrett
#date			:20151228
#version		:1
#usage			:python day8.py
#notes			:
#python_version	:2.6.6
#==============================================================================

import re

#f = open('test.txt')
f = open('input.txt')


def count_total_chars(line):
    print len(line)

def count_mem_chars(line):
    raw_length = len(line)
    mem_length = raw_length-2

    match = re.findall(r'\\(.)',line)
    
    for m in match:
        #print m
        if m == 'x':
            print 'hex'
            mem_length -= 3
        elif m == '"':
            print 'quote'
            mem_length -= 1
        else:
            print 'bslash'
            mem_length -= 1
    print raw_length
    print mem_length
    return raw_length, mem_length



total_raw_length = 0
total_mem_length = 0
for line in f:
    line = line.rstrip('\n') # removes trailing \n
    print line
    #count_total_chars(line)
    line_raw_length, line_mem_length = count_mem_chars(line)
    total_raw_length += line_raw_length
    total_mem_length += line_mem_length

print total_raw_length
print total_mem_length
print total_raw_length - total_mem_length 
