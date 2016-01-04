#!/usr/bin/python
#title			:day18.py
#description		:advent of code day 18
#author			:Mike Jarrett
#date			:20160101
#version		:1
#usage			:python day18.py
#notes			:
#python_version	:2.6.6
#==============================================================================

import re

f = open('test.txt')
steps = 4
#f = open('input.txt')
#steps = 100


data = f.read().splitlines()
        
#print data
ndata = []
for datum in data:
    datum = list(datum)
    ndata.append(datum)  # ndata is indexed from the top left corner [y][x]
 

 

#print ndata



#define neighbours
def neighs((y,x),m):
    return [ i for i in [(y, x+1), (y, x-1), (y+1, x), (y-1, x), (y-1,x-1), (y-1,x+1), (y+1,x-1), (y+1,x+1)] if m-1 >= i[0] >= 0 and m-1 >= i[1] >=0 ]

#print neighs((6,6),len(data))
#iterate through
#ndata[0][0] += '#'

def ifon(y,x,neighs,it):
    count = 0
#    print 'neighbours'
    for neigh in neighs:
#        print ndata[neigh[0]][neigh[1]][it-1]
        if ndata[neigh[0]][neigh[1]][it] == '#':
            count += 1
    if count == 2 or count == 3:
        return '#'
    else:
        return '.'


def ifoff(y,x,neighs,it):
    count = 0
#    print 'neighbours'
    for neigh in neighs:
#        print ndata[neigh[0]][neigh[1]][it-1]
        if ndata[neigh[0]][neigh[1]][it] == '#':
            count += 1
    
    #print 'count = ' + str(count)
    if count == 3:
        return '#'
    else:
        return '.'


#fresh ndata for part 2
ndata2 = ndata

for q in range(steps):
    for y in range(len(data)):
        for x in range(len(data)):
            #print y, x
        
            if ndata[y][x][q] == '#':
                #print 'on'
                #print ifon(y,x,neighs((y,x),len(data)))
                ndata[y][x] += ifon(y,x,neighs((y,x),len(data)),q)
               
            elif ndata[y][x][q] == '.':
                #print 'off'
                #print ifoff(y,x,neighs((y,x),len(data)))
                ndata[y][x] += ifoff(y,x,neighs((y,x),len(data)),q)


            #part 2
#            if (y == 0 and x == 0) or (y == 0 and x == len(data)) or ( y == len(data) and x == 0) or (y == len(data) and x == len(data)):
#                ndata2[y][x] += '#'


#            elif ndata2[y][x][q] == '#':
#                ndata2[y][x] += ifon(y,x,neighs((y,x),len(data)),q)
            
#            elif ndata2[y][x][q] == '.':
#                ndata2[y][x] += ifoff(y,x,neighs((y,x),len(data)),q)




    #print 'iteration = ' + str(q+1)
    #print ndata
    #print ndata[0]
    #print ndata[0][0]
    #print ndata[0][0][q]
    #print ndata[:][:][q]
output = []
rawout = ''
for y in range(len(data)):
    outputline = []
    for x in range(len(data)):
        outputline.append(ndata[y][x][steps])
        rawout += ndata[y][x][steps]
    output.append(outputline)
    print outputline
#print output
print rawout
print len([ x for x in rawout if x == '#' ])

print ndata2
