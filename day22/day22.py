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

effects = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

results = {}
#provide hitpoints, damage given and defense for each player     
def fight(mhp,mdam,mdef,bhp,bdam,bdef):

    bhp -= max([mdam - bdef,1])
    mhp -= max([bdam - mdef,1])

    return mhp,bhp

def init():
    # each element of future should be a list [damage dealt, armour received, health received, newmana]. Max effect length is 6 turns, so only need to keep track of next 6 turns
    future = [[0]*4,[0]*4,[0]*4,[0]*4,[0]*4,[0]*4]    

    # initialize stats
    myhp = 50
    mymana = 500
    bosshp = 71
    bossdam = 10

    return future, [myhp,mymana,bosshp,bossdam] 

def turn(future, stats):


    print "--------------------"
    print "--------------------"
    

#    print effects
    #choose a random spell
    goodspells = [ x for x in spells if x[1] <= stats[1] ]  #only choose from spells you can afford
    goodspells = [ x for x in goodspells if effects[x[0]] <= 1 ] # and spells that aren't currently ongoing

#    print "active spells: "
#    print [ x[0] for x in spells if effects[x[0]] >0 ]


    spell = random.choice(goodspells)
    print "spell %d" % (spell[0])
#    print spell
    effects[spell[0]] = spell[2] 
#    print effects
    
        

    #add to future according to length of effect
    for i in range(spell[2]):

        future[i][0] += spell[3]  #damage
        future[i][1] += spell[4]  #armour
        future[i][2] += spell[5]  #health
        future[i][3] += spell[6]  #newmana

#    print future
#    print stats

    #run fight(mhp,mdam,mdef,bhp,bdam,bdef)
    mhp,bhp = fight(stats[0],future[0][0],future[0][1],stats[2],stats[3],0)
#    print "hitpoints after round %d, %d" % (mhp, bhp)
    mymana = stats[1] - spell[1]
#    print "mana after spending it: %d" % mymana
    mymana += future[0][3]
#    print "mana after recharge: %d" % mymana
    mhp += future[0][2]
#    print "hp after health boost: %d" % mhp

    
    #update future list mylist.insert(0, mylist.pop(5))
    future.pop(0) #remove first element from list
    future.append([0]*4) #add a 6th day to the end of the list
#    print future

    # update effects
    for k in effects.keys():
        effects[k] = max(effects[k]-1, 0)

    #update stats
    stats = [mhp,mymana,bhp,stats[3]]

    if stats[1] < 53 or mhp <= 0 or bhp <= 0:
        return future, stats, True, spell[0], spell[1]
    else:
        return future, stats, False, spell[0], spell[1]

def sim_match():
    #initialize stats
    f,s = init()
    isOver = False
    spellorder = ''
    manaspent = 0

    while not isOver:
        f,s, isOver, lastSpell, mana= turn(f,s)
        spellorder += str(lastSpell)
        manaspent += mana
        #print s
    #print spellorder
    return spellorder, manaspent
    
for i in range(100):
    matches = {}
    a, b = sim_match()
    matches[a] = b

print matches

