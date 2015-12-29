#!/usr/bin/python
#title			:day11.py
#description		:advent of code day 11
#author			:Mike Jarrett
#date			:20151229
#version		:1
#usage			:python day11.py
#notes			:
#python_version	:2.6.6
#==============================================================================

import string

#password = 'abbcdizz'
alpha = string.ascii_lowercase
#letters = [ i for i in list(alpha) if i != 'i' and i != 'l' and i != 'o']
letters = list(alpha)
badletters = [ 'i','l','o' ]

def sanitize(pswd):
    for i, c in enumerate(pswd):
        
        if i == 0:
            spswd = ''
            epswd = pswd[i+1:]
        else:
            spswd = pswd[:i]
            epswd = pswd[i+1:]

#        print spswd, epswd

        while c in badletters:
            nchar = letters[letters.index(c)+1]
        


def iterate(pswd):

    for i, c in enumerate(pswd):
        #break pswd into before, after and working char
        ochar = pswd[-i-1]
        if i == 0:
            spswd = pswd[:-i-1]
            epswd = ''
        else:
            spswd = pswd[:-i-1]
            epswd = pswd[-i:]

        #print spswd, epswd


        if pswd[-i-1] != letters[len(letters)-1]:  #if the last character in the password isn't z, iterate it once

            ochar = pswd[-i-1] 
            nchar = letters[letters.index(ochar)+1]
            
            #print char, nchar
            pswd = spswd + nchar + epswd
            break
        else:

            nchar = letters[0]
            pswd = spswd + nchar + epswd
            #print "elsepswd " + pswd
    return pswd


def run3(pswd):
    for i,c in enumerate(pswd):
        if i < len(pswd)-2:
            test = pswd[i:i+3]
            if test in alpha:
                return True
    return False

def nobads(pswd):
    for c in pswd:
        if c in badletters:
            return False
    return True

def twodoubs(pswd):
    firstdoub = ''
    for i, c in enumerate(pswd):
        if i < len(pswd)-1:
            test = pswd[i:i+2]
      #      print test
            if test[0] == test[1] and firstdoub and test != firstdoub:
                return True
            elif test[0] == test[1]:
                firstdoub = test
    return False


def goodpass(pswd):
    if twodoubs(pswd) and run3(pswd) and nobads(pswd):
        return True
    else:
        return False


            


def findpass(pswd):
    pswd = iterate(pswd)
    while goodpass(pswd) != True:
        pswd = iterate(pswd)
        #print pswd
    return pswd
    

#print 'abcdefgh ' + findpass('abcdefgh'), " abcdffaa"
#print 'ghijklmn ' + findpass('ghijklmn'), " ghjaabcc"
#sanitize('iolio')
print 'part 1: ' + findpass('vzbxkghb')
print 'part 2: ' + findpass(findpass('vzbxkghb'))

###################################
# Test function
def test():
    print str(goodpass('hijklmmn')) + " False"
    print str(goodpass('abbceffg')) + " False"
    print str(goodpass('abbcegjk')) + " False"
    print str(goodpass('abcdffaa')) + " True"
    print str(goodpass('ghjaabcc')) + " True"
  
    print str(iterate('abcdefgh')) + " abcdffaa"
    print str(iterate('ghijklmn')) + " ghjaabcc"  
  
#test()
#####################################
