#!/usr/bin/python
#title			:day5.py
#description		:day 5 advent of code
#author			:Mike Jarrett
#date			:20151223
#version		:1
#usage			:python day5.py
#notes			:
#python_version	:2.6.6
#==============================================================================

#import re

vowels = [ 'a', 'e', 'i', 'o', 'u' ]
badstrings = [ 'ab', 'cd', 'pq', 'xy' ]

def threevowels(line):
    threevow = False
        
    count = 0
#    print line

    for c in line:
            
        if c in vowels:
            #print vowel
            count += 1
            #print count
            #print line
            if count == 3:
                threevow = True
                #print line
                break
    return threevow

def hasdoubles(line):
    hasdoubs = False
    for i, c in enumerate(line):  #i gives index, c gives character

        if i != 0:
            if line[i] == line[i-1]:

                hasdoubs = True 
        #    break
    return hasdoubs
        
def nobads(line):
    nobad = True

    for i, c in enumerate(line):
        if i != 0:
            pair = line[i-1] + line[i]
            if pair in badstrings:
                #print pair
                nobad = False
    return nobad


def hasdoubdoub(line):
    doubdoub = False
    for i, c in enumerate(line):
        if i != 0:
            pair = line[i-1] + line[i]
            #print pair + ' ' + line + ' ' + line[:i-1] + line[i+1:]
            if pair in line[:i-1] or pair in line[i+1:]:
                print pair
                doubdoub = True
                
    return doubdoub

def hassep(line):
    sep = False
    for i, c in enumerate(line):  #i gives index, c gives character
        if i > 1:
            if line[i] == line[i-2]:
                sep = True 
    return sep



def goodstrings():

    f = open('input.txt')
#    f = [ 'qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy', 'urrxxebxrthtjvib' ] # part 2 test
#    f = [ 'ugknbfddgicrmopn', 'jchzalrnumimnmhp' , 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb' ] #part 1 test

    goodlines = 0
    goodlines2 = 0
    for line in f:
        #print line

        if threevowels(line) and hasdoubles(line) and nobads(line):
        #if nobads(line):
            goodlines += 1
            
            #print 'part 1' + line


        if hasdoubdoub(line) and hassep(line):
            goodlines2 +=1
            print line

    print 'part 1 ', goodlines
    print 'part 2 ', goodlines2



goodstrings()
