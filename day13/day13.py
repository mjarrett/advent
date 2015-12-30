#!/usr/bin/python
#title			:day13.py
#description		:day 13 of advent of code
#author			:Mike Jarrett
#date			:20151229
#version		:1
#usage			:python day13.py
#notes			:
#python_version	:2.6.6
#==============================================================================
import re
import itertools as it

#f = open('test.txt')
f = open('input.txt')



def read_in(f):
    happy = {}
    people = []    
    for line in f:
        p = re.search('(\w+) would gain (\d+) happiness units by sitting next to (\w+).',line)
        m = re.search('(\w+) would lose (\d+) happiness units by sitting next to (\w+).',line)
        #print m.group(1), m.group(2), m.group(3)
        if p:
            happy[(p.group(1),p.group(3))] = int(p.group(2))
            #print p.group(1), p.group(2), p.group(3)
            people.append(p.group(1)) #add people to people list
            
        if m:
            happy[(m.group(1),m.group(3))] = -1*int(m.group(2))
            #print m.group(1), m.group(2), m.group(3)
            people.append(m.group(1)) #add people to people list
                
    people = list(set(people)) #remove duplicates

    return people, happy


def permute(people, happy):
    perms = list(it.permutations(people,len(people))) #list of permutations
    changes = []
    for perm in perms:
        #print perm
        table = 0
        for i,p in enumerate(perm):
            if i < len(perm)-1:
                table += happy[(perm[i],perm[i+1])] + happy[(perm[i+1],perm[i])]
            if i == len(perm)-1:
                table += happy[(perm[i],perm[0])] + happy[(perm[0],perm[i])]
        changes.append(table)
    return max(changes)

p,h = read_in(f)

print "part 1: " + str(permute(p,h))

for person in p:
    h[(person,'me')] = 0
    h[('me',person)] = 0

p.append('me')
print "part 2: " + str(permute(p,h))
