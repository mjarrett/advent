#!/usr/bin/python
#title			:day3.py
#description		:Day 3 of Advent of code
#author			:Mike Jarrett
#date			:20151222
#version		:1
#usage			:python day3.py
#notes			:
#python_version	:2.6.6
#==============================================================================

import sys


def calc_dirs(infile):
        
    coord_visits = {}
    coord = [0, 0] #starting coord, updated after each move
        
        
    # end the origin into the dic
    coord_visits[tuple(coord)] = 1
        
    with open(infile) as f:
        while True:
            c = f.read(1)
            if c == '^':
                #print 'up'
                coord[1] += 1                
            elif c == 'v':
                #print 'down'
                coord[1] += -1                    
            elif c == '>':
                #print 'right'
                coord[0] += 1                  
            elif c == '<':
                #print 'left'
                coord[0] += -1                    
            else: break
                    
                    
            #at this point we've resolved the current coordinate
            #print tuple(coord)
            coord_tup = tuple(coord)
            if coord_tup in coord_visits:
                coord_visits[coord_tup] += 1
            else:
                coord_visits[coord_tup] = 1
    return coord_visits
                        

def sort_robo():
    out_santa = open('santa_dirs.txt','a')
    out_robo = open('robo_dirs.txt','a')

    robo = True



    with open('input.txt') as f:
        while True:
            c = f.read(1)


            if c == '^' or c == 'v' or c == '<' or c == '>':
                #print c
                robo = not robo
                
                if robo == True:
                    out_robo.write(c)
                elif robo == False:
                    out_santa.write(c)


            else:
                    # print 'something is wrong'                                                                                 
                out_santa.close()
                out_robo.close()
                f.close()
                #print 'break'
                break

    santa_dic = calc_dirs('santa_dirs.txt')
    robo_dic = calc_dirs('robo_dirs.txt')

    both_dic = santa_dic # initialize combined dict starting with santa, then add robo
    for key in robo_dic:
        if key in santa_dic:
            both_dic[key] = robo_dic[key] + santa_dic[key]
        else:
            both_dic[key] = robo_dic[key]

    return both_dic

#part one answer
print len(calc_dirs('input.txt'))

#part two answer
print len(sort_robo())

