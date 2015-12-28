#!/usr/bin/python
#title			:day7.py
#description		:advent of code day7
#author			:Mike Jarrett
#date			:20151225
#version		:1
#usage			:python day7.py
#notes			:
#python_version	:2.6.6
#==============================================================================

import re


f = open('input.txt')
#f = open('test.txt')

wires = {}
connects = []



#this section loads all the lines into a list
for line in f:
    m = re.match(r'(\w+)\s(\w*)\s?(\w*)\s?->\s(\w+)',line)
    
    #print m.group(1), m.group(2), m.group(3), m.group(4)
    #print line
    #print m.group(1)
    #print m.group(2)
    #print m.group(3)
    #print m.group(4)

    if m.group(2) == '' and m.group(3) == '':
        #direct assignment
        try: 
            int(m.group(1))
            connects.append(('start',m.group(1),'','',m.group(4)))
        except:
            connects.append(('assign',m.group(1),'','',m.group(4)))
        
    elif m.group(2) != '' and m.group(3) == '':
        #NOT xx = yy
        #print line
#        notswitch(m.group(2),m.group(4))
        try:
            int(m.group(2))
            connects.append(('not',int(m.group(2)),'','',m.group(4)))
        except:
            connects.append(('not',m.group(2),'','',m.group(4)))

    else:
        # xx OR yy = zz
#        comboswitch(m.group(1),m.group(2),m.group(3),m.group(4))
        try:
            x = int(m.group(1))
            t = 'combo_int'
        except:
            x = m.group(1)
            t = 'combo'
        #try:
        #    y = int(m.group(3))
        #    t = 'combo_int'
        #except:
        #    y = m.group(3)
        #    t = 'combo'
        y = m.group(3)
        connects.append((t,x,m.group(2),y,m.group(4)))
        

#print connects

#now create a key in the dict for each wire
for connect in connects:
    if connect[0] != 'start': wires[connect[1]] = ''
    wires[connect[4]] = ''
    if connect[3] != '':

        try:
            int(connect[3])            
        except:
            wires[connect[3]] = ''
    

# now find starting points in connects and assign wire values
for connect in connects:
    if connect[0] == 'start': 
        #wires[connect[4]] = int(connect[1])
        wires[connect[4]] =  BitArray('0b'+'{0:016b}'.format(int(connect[1])))
# fxn to find wires that have been assigned and return list
def findempty():
    empty_wires = []
    for k, v in wires.items():
        if v == '':
            empty_wires.append(k)
    return empty_wires

def findfilled():
    filled_wires = []
    for k, v in wires.items():
        if v != '':
            filled_wires.append(k)
    return filled_wires

# fxn to find connections that are ready to be evaluated
def findnext():
    todo = []
    for connect in connects:
        if connect[0] == 'combo' and connect[1] in findfilled() and connect[3] in findfilled() and connect[4] in findempty():
            #print connect
            todo.append(connect)
        elif connect[0] == 'combo_int' and ( connect[1] in findfilled() or connect[3] in findfilled() ) and connect[4] in findempty():
            todo.append(connect)
        elif connect[1] in findfilled() and (connect[2] == 'LSHIFT' or connect[2] == 'RSHIFT') and connect[4] in findempty():
            todo.append(connect)
        elif connect[1] in findfilled() and connect[0] == 'not' and connect[4] in findempty():
            todo.append(connect)
        elif connect[0] == 'assign' and connect[1] in findfilled() and connect[4] in findempty():
            todo.append(connect)
    return todo





def eval(c):
    #print c
    if c[2] == 'AND' and c[0] == 'combo':
        wires[c[4]] = wires[c[1]] & wires[c[3]]
    elif c[2] == 'AND' and c[0] == 'combo_int':
        wires[c[4]] = c[1] & wires[c[3]] 
    elif c[2] == 'OR':        
        wires[c[4]] = wires[c[1]] | wires[c[3]]
    elif c[2] == 'LSHIFT':
        wires[c[4]] = wires[c[1]] << int(c[3])
    elif c[2] == 'RSHIFT':
        wires[c[4]] = wires[c[1]] >> int(c[3])
    elif c[0] == 'not':
        wires[c[4]] = ~wires[c[1]] 
    elif c[0] == 'assign':
        wires[c[4]] = wires[c[1]]



# while there are still connects to eval, check for good connections and evaluate
while findnext():

    for c in findnext():
        print c
        print wires['lx']
        print wires['a']
#        print sorted(findfilled())
        eval(c)

print wires['a']
#print wires
print sorted(findfilled())

for connect in connects:
    if connect[1] in findfilled() and connect[4] in findempty():
        print '1'
        print connect
    if connect[3] in findfilled() and connect[4] in findempty():
        print connect
