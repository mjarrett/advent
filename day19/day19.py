#!/usr/bin/python
#title			:day19.py
#description		:advent of code day 19
#author			:Mike Jarrett
#date			:20160104
#version		:1
#usage			:python day19.py
#notes			:
#python_version	:2.6.6
#==============================================================================

import re

f = open('input.txt')
#f = open('test.txt')
trans = []


for line in f:
#    print line
    m = re.search('(\w+) => (\w+)', line)
    if m:
        trans.append((m.group(1),m.group(2)))

    n = re.search('^(\w+)$',line)
    if n:
        mol = n.group(1)

results = []
for tran in trans:
#    results.append(mol.replace(tran[0],tran[1]))
    #print tran
    for i, c in enumerate(mol):
        if i < len(mol) and mol[i] == tran[0]:
            #print mol[:i] + " " + mol[i] + " " + mol[i+1:]
            results.append(mol[:i]+tran[1]+mol[i+1:])
        
        elif i < len(mol)-1 and mol[i] + mol[i+1] == tran[0]:
            #print mol[:i] + " " + mol[i]+mol[i+1] + " " + mol[i+2:]
            results.append(mol[:i]+tran[1]+mol[i+2:])

#print results
#print len(results)

print len(set(results))




#################3
#oart 2         #

def f(it):
    return len(it[1])

strans = sorted(trans, key=f, reverse=True)

def iter(m):

    while m != 'e':

        for tran in strans:
            
            if tran[1] in m:
                print tran
                m.replace(tran[1],tran[0])
                
            
            
        print m


print iter(mol)
