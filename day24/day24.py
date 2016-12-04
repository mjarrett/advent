#!/usr/bin/env python3
import itertools


#input = open('input.txt')
weights = open('input.txt').read().split()
weights = [ int(x) for x in weights ]
weights = sorted(weights,reverse=True)
print(weights)

def part1(weights):
    target = int(sum(weights)/3)
    for i in range(3):
        combs = list(itertools.combinations(weights,i))
        t = 0
        for j in combs:
            




part1(weights)
