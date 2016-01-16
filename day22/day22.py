#!/usr/bin/python
#title			:day22.py
#description		:advent of code day 22
#author			:Mike Jarrett
#date			:20160109
#version		:1
#usage			:python day22.py
#notes			:
#python_version	:2.7.6
#==============================================================================
import itertools
import random



#   (id, mana, turns, damage, armour,health,newmana)
missile = [1,53,1,4,0,0,0]
drain   = [2,73,1,2,0,2,0]
shield =  [3,113,6,0,7,0,0]
poison =  [4,173,6,3,0,0,0]
recharge =[5,229,5,0,0,0,101]
spells =  [missile,drain,shield,poison,recharge]


#provide hitpoints, damage given and defense for each player     
def fight(mhp,mdam,mdef,bhp,bdam,bdef):

    mhp -= max([bdam - mdef,1])
    bhp -= max([mdam - bdef,1])

    return mhp,bhp

def init():
    # each element of future should be a list [damage dealt, armour received, health received, newmana]
    future = [[0]*4,[0]*4,[0]*4,[0]*4,[0]*4,[0]*4,]    

    # initialize stats
    myhp = 50
    mymana = 500
    bosshp = 71
    bossdam = 10

    return future, [myhp,mymana,bosshp,bossdam] 

def turn(future, stats):
    #choose a random spell
    goodspells = [x for x in spells if x[1] <= stats[1]]  #only choose from spells you can afford
    
    try:
        spell = random.choice(goodspells)
        print "spell %d" % (spell[0])
        print spell
    except IndexError:
        spell = [0]*7
        print "Out of mana"


    #add to future according to length of effect
    for i in range(spell[2]):
        #print i
        future[i][0] += spell[3]  #damage
        future[i][1] += spell[4]  #armour
        future[i][2] += spell[5]  #health
        future[i][3] += spell[6]  #newmana
        

    print stats
    print future
    #run fight(mhp,mdam,mdef,bhp,bdam,bdef)
    mhp,bhp = fight(stats[0],future[0][0],future[0][1],stats[2],stats[3],0)
    print "hitpoints after round %d, %d" % (mhp, bhp)
    mymana = stats[1] - spell[1]
    print "mana after spending it: %d" % mymana
    mymana += future[0][3]
    print "mana after recharge: %d" % mymana
    mhp += future[0][2]
    print "hp after health boost: %d" % mhp

    
    #update future list mylist.insert(0, mylist.pop(5))
    future.pop(0) #remove first elemet from list
    future.append([0]*4) #add a 6th day to the end of the list

    #update stats
    stats = [mhp,mymana,bhp,stats[3]]

    return future, stats

def sim_match():
    #initialize stats
    f,s = init()
    #print turn(f,s)
    
    while s[0]>0:
        f,s = turn(f,s)
        print s
    return s


sim_match()

#while True:
#    s = sim_match()

#    if s[2] < 0:
#        print s
#        break


