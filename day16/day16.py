#!/usr/bin/python                                                                                                                                   
#title                  :day16.py                                                                                                                   
#description            :advent of code day 16                                                                                                      
#author                 :Mike Jarrett                                                                                                               
#date                   :20151230                                                                                                                   
#version                :1                                                                                                                          
#usage                  :python day16.py                                                                                                            
#notes                  :                                                                                                                           
#python_version :2.6.6                                                                                                                              
#==============================================================================                                                                     
import re


info = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}



f = open('input.txt')
for line in f:
    m = re.search('Sue (\w+): (\w+): (\d+), (\w+): (\d), (\w+): (\d+)',line)
    if m:
        #            print m.group(3), info[m.group(2)]
        if int(m.group(3)) == info[m.group(2)] and int(m.group(5)) == info[m.group(4)] and int(m.group(7)) == info[m.group(6)]:
            print "part 1: " + str(m.group(1))
                

        tpls = [(m.group(2), m.group(3)), (m.group(4),m.group(5)), (m.group(6),m.group(7))]
        test = 0
        for tpl in tpls:
            #print line
            if tpl[0] == 'trees' or tpl[0] == 'cats':
                #print "lessthan"
                #print tpl[1], info[tpl[0]]
                if int(tpl[1]) > info[tpl[0]]:
                    test += 1
            elif tpl[0] == 'pomerianians' or tpl[0] == 'goldfish':
                if int(tpl[1]) < info[tpl[0]]:
                    test += 1
            else:
                if int(tpl[1]) == info[tpl[0]]:
                    test += 1
            
            #print test
            if test == 3:
#                print info
#                print line
                print "part 2: " + str(m.group(1))



