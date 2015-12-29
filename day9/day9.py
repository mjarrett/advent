#!/usr/bin/python
#title			:day9.py
#description		:advent of code day 9
#author			:Mike Jarrett
#date			:20151228
#version		:1
#usage			:python day9.py
#notes			:
#python_version	:2.6.6
#==============================================================================

import itertools as it

f = open("input.txt")
#f = open("test.txt")

distances = {}
stars = []
for line in f:
    words = line.split()
#    print words[0], words[2], words[4]
    distances[tuple(sorted([words[0],words[2]]))] = words[4] #keys are star pairs in alphabetical order
    stars.append(words[0])
    stars.append(words[2])

stars = list(set(stars)) #remove duplicates
perms = list(it.permutations(stars,len(stars))) #list of permutations

#print perms
ds = []
for perm in perms:
#    print int(distances[tuple(sorted([perm[0],perm[1]]))]) + int(distances[tuple(sorted([perm[1],perm[2]]))]) #special case
    
    d = 0
    for i in range(len(stars)-1):
        d += int(distances[tuple(sorted([perm[i],perm[i+1]]))])
    #print d
    ds.append(d)

print "part 1 " + str(min(ds))
print "part 2 " + str(max(ds))
