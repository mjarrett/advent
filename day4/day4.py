#!/usr/bin/python
#title			:day4.py
#description		:Advent of code day 4
#author			:Mike Jarrett
#date			:20151222
#version		:1
#usage			:python day4.py
#notes			:
#python_version	:2.6.6
#==============================================================================
import hashlib
import itertools

def find_hash():

    m = hashlib.md5() # create has object
    secret_key = 'bgvyzdsv' #define my key
    
    for i in itertools.count(0):
        test_hash = secret_key + str(i) # add test nuber to key
        m.update(test_hash) # hash the test string

        mh = m.hexdigest()
        if mh[0:6] == '0':
            print mh # print the test hash
            break



    return mh


find_hash()
