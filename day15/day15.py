#!/usr/bin/python
#title			:day15.py
#description		:advent of code day 15
#author			:Mike Jarrett
#date			:20151230
#version		:1
#usage			:python day15.py
#notes			:
#python_version	:2.6.6
#==============================================================================
import re
import itertools as it

#fn = 'test.txt'
fn = 'input.txt'
total_tspns = 100
ingredients = {}
ingredients_list = []
cats = ['capacity','durability','flavor','texture']

def read_in(fn):
    f = open(fn)
    for line in f:
        m = re.search('(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)',line)
        if m:
            ingredients[m.group(1)] = ( int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), int(m.group(6)))
            ingredients_list.append(m.group(1))
    return ingredients, ingredients_list


ings, ing_list = read_in(fn)    
n_ing = len(ing_list)
print ings

perms = [ x for x in list(it.permutations(range(total_tspns+1),n_ing)) if sum(x) == 100 ]
results = [0]*len(cats)
result = []
result2 = []
for perm in perms: # for each permutation
    cals = 0
    for i, item in enumerate(ing_list): # for each ingredient
        for j, cat in enumerate(cats): # for each category
            #print perm
            #print item
            #print cat
            #print perm[i]
            #print ings[item][j]
            #print perm[i]*ings[item][j]
            #print '---------------------'
            results[j] += perm[i]*ings[item][j]

        #Part 2: check calories before appending
        cals += perm[i]*ings[item][4]
    #print perm
    #print results
    r = 1
    for k in results:
        
        if k < 0:
            r = 0
        else:
            r *= k 
    result.append(r)
    results = [0]*len(cats)

    if cals == 500:
        result2.append(r)
    



    #print result
    
    #print '-------------------'

print "Part 1: " + str(max(result))
print "Part 2: " + str(max(result2))
