#!/usr/bin/env python3
import re
import operator
from collections import Counter
from string import ascii_lowercase as alphabet
data = open('/Users/msj/github/adventofcode2016/day4.txt','r')#.read()#.split()

def real_rooms():
    #total = 0
    rooms = []
    for line in data:
        #print(line)
        m = re.match('(\D+)(\d+)\[(\w+)\]',line)
        if m:
            #print(line)
            name = m.group(1)
            sname = name.replace('-','')
            sector = int(m.group(2))
            checksum = m.group(3)
#            print(sname,sector,checksum)

            letters = sorted(Counter(sname).items(), key=operator.itemgetter(1),reverse=True)
            letters = sorted(letters,key=lambda x: (-x[1],x[0])) # sort by number, then alphabetically
            #find 5th most common letter count:
            mincount = letters[4][1] # this is the minimum count allowed in checksum
            mincountl = [ x[0] for x in letters if x[1] == mincount ] #list of letters with mincount
            #populate mycheck with what you'll test the checksum against
            mycheck = [ x[0] for x in letters if x[1] > mincount ] #guarenteed letters
            mycheck = mycheck+mincountl[:5-len(mycheck)] # fill remaining spots with mincount letters alphabetically ordered
            mycheck = ''.join(mycheck) #turn list into string
            # check checksum
            if mycheck == checksum:
                #print('Real room!')
                #total = total + sector
                rooms.append([name,sector])
            #else: print('Fake room!')
    #print(total)
    return rooms
good_rooms = real_rooms()
print('Part 1: {}'.format(sum( [ x[1] for x in good_rooms ]  )))

def shift_letter(letter,sector):

    if alphabet.find(letter)+sector%26 < 26:
        nletter = alphabet[alphabet.find(letter) + sector%26]
    else: nletter = alphabet[alphabet.find(letter)+sector%26 - 26]

    return nletter

def shift_word(word,sector):
    nword = ''
    for letter in word:
        nword = nword + shift_letter(letter,343)
    return nword

def part2():

    for room in good_rooms:
        name = room[0].split('-')
        sector = room[1]
        nname = [ shift_word(word,sector) for word in name ]
        # the question doesn't give the explicit room name so have to check some word fragments
        if any('object' in n  or 'north' in n  or 'stor' in n for n in nname):
            print(nname,sector)
    #print(shift_word(word,343))

#print(shift_letter('z',343))
part2()
