#!/usr/bin/python
#title			:day14.py
#description		:advent of code day14
#author			:Mike Jarrett
#date			:20151229
#version		:1
#usage			:python day14.py
#notes			:
#python_version	:2.6.6
#==============================================================================
import re

#fn = 'test.txt'
#time = 1000

fn = 'input.txt'
time = 2503

def read_in(fn):
    f = open(fn)
    deers = []
    for line in f:
        m = re.search('(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.',line)
        if m:
            #print m.group(1), m.group(2), m.group(3), m.group(4)
            deers.append([m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))])
    f.close()
    return deers

def how_far(deer,t):
#    print deer
    cycle = deer[2] + deer[3] # time for one full cycle
    cycles = t/cycle  # number of full cycles completed
    remain = t % cycle  # number of seconds left over

#    print cycle, cycles, remain
    if remain < deer[2]:
        time_flying = cycles*deer[2] + remain
        
    else:
        time_flying = cycles*deer[2] + deer[2]

#    print time_flying
    return time_flying * deer[1]

#print read_in(f)
results = []
for d in read_in(fn):
    results.append(how_far(d,time))
print "part 1: " + str(max(results))


def name(t):
    return t[1]

results2 = {}
#results_persec = {}
#initialize results dict
for d in read_in(fn):
    results2[d[0]] = 0
#    results_persec[d[0]] = 0

for t in range(1,time+1):
    results_persec = []
    #print t
    for d in read_in(fn):
        #print d[0], str(t)
        #print how_far(d,t)
        results_persec.append([d[0],how_far(d,t)])
        

    #if results_persec[0][1] == results_persec[1][1]:
    #    print sorted(results_persec, key=name)
    
    # find top distance at each interval
    topdist = sorted(results_persec, key=name, reverse=True)[0][1]
    
    #loop over each deer, if == topdist add to dict
    for d in results_persec:
        if d[1] == topdist:
            results2[d[0]] += 1


#print results2
print "part 2: " + str(max(results2.values()))
