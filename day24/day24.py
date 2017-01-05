#!/usr/bin/env python3

import itertools as it


#input = open('input.txt')
with open('input.txt') as f:
    weights = f.read().split()
    weights = [ int(x) for x in weights ]
    weights = sorted(weights,reverse=True)
    #print(weights)

def prod(tup):
    prod = 1
    for t in tup:
        prod = prod*t
    return prod


def soln(weights,part):
    if part == 1:
        N = 3
    elif part == 2:
        N = 4
    else:
        return "Input error"

    target = int(sum(weights)/N)


    if target in weights:
        return target

    i = 1
    while True:
        sums = [ (sum(comb),prod(comb)) for comb in list(it.combinations(weights,i)) if sum(comb) == target ]
        if len(sums) > 0:
            return sorted(sums,key=lambda x:x[1])[0][1]
        i += 1

print(soln(weights,2))
