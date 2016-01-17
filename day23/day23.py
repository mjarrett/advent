#!/usr/bin/python
#title			:day23.py
#description		:Advent of code day 23
#author			:Mike Jarrett
#date			:20160116
#version		:1
#usage			:python day23.py
#notes			:
#python_version	:2.7.6
#==============================================================================


import re

def interp(cmd, regs, i):
    if cmd[0] == 'hlf':
        regs[cmd[1]] = int(regs[cmd[1]])/2
        i += 1
    elif cmd[0] == 'tpl':
        regs[cmd[1]] = int(regs[cmd[1]])*3
        i += 1
    elif cmd[0] == 'inc':
        regs[cmd[1]] += 1
        i += 1
    elif cmd[0] == 'jmp':
        i += int(cmd[1])
    elif cmd[0] == 'jie':
        if int(regs[cmd[1]]) == 0 or int(regs[cmd[1]]) % 2 == 0:
            i += int(cmd[2])
        else: i += 1
    elif cmd[0] == 'jio':
        if int(regs[cmd[1]]) == 1:
            i += int(cmd[2])
        else: i+= 1
    else: print "BAD COMMAND"
    return regs, i

def main():
     
    regs = {'a':1, 'b':0}
    instructs = []
    f = open('input.txt','r')
    i = 0

    for line in f:
        m = re.search('(\w+) ([\+-]?\w+),?\s([\+-]?\w*)',line)
        if m:

            instructs.append( [m.group(1), m.group(2), m.group(3)] )


    
    while i < len(instructs):
        print regs
        print instructs[i]

        regs, i = interp(instructs[i],regs, i)
    print regs

if __name__ == "__main__":
    main()
    


    
