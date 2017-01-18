#!/usr/bin/env python3
code = 20151125


def nextcode(code):
    return (code*252533)%33554393

def get_address(loc):
    row=loc[0]
    col=loc[1]

    c = (col*col+col)/2
    for i in range(1,row):
        c = c + col
        col += 1
    return int(c)

#print(get_address((2947,3029)))
#print(get_address((1,2)))

for i in range(1,get_address((2947,3029))):
#for i in range(1,get_address((6,3))):
    code = nextcode(code)

print(code)
