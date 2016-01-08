#!/usr/bin/python
#title			:day20.py
#description		:advent of code day 20
#author			:Mike Jarrett
#date			:20160107
#version		:1
#usage			:python day20.py
#notes			:
#python_version	:2.6.6
#==============================================================================

top = 34000000
#top = 180

house = 1
presents = 0



def part2(t,p,p2):
    houses = {}
    for house in range(1,t/10):
        houses[house] = 0


    for elf in range(1,t/10):
        count = 0 #count houses visited for part 2
        for house in range(elf,t/10,elf):
#            print house
            houses[house] += elf*p
            count += 1
            #print count
            if p2 and count == 50:
                break
                


    return houses

print "part 1: %d" % min([k for k,v in  part2(top,10,False).items() if v >= top ])
print "part 2: %d" % min([k for k,v in part2(top,11,True).items() if v >= top ])
