#!/usr/bin/python
#title			:day10.py
#description		:advent of code day 10
#author			:Mike Jarrett
#date			:20151228
#version		:1
#usage			:python day10.py
#notes			:
#python_version	:2.6.6
#==============================================================================

datum = '1113222113'
test = '1'

def looksay(look):
    say = []
    count = 1
    for i,c in enumerate(look):
    

            
        if i != len(look)-1 and look[i] == look[i+1]:
            count += 1
        #    print c, str(count)
        elif i != len(look)-1: 
       #     print c, str(count)
            say.append(str(count))
            say.append(look[i])
            count = 1
        else:
      #      print c, str(count)
            say.append(str(count))
            say.append(look[i])

    #say.append(count)
    #say.append(c)
    return "".join(say)


def recurse(n, start):
    for i in range(n):
        start = looksay(start)
        #print start
    return start

print datum
print "part 1: " + str(len(recurse(40, datum)))
print "part 2: " + str(len(recurse(50, datum)))
