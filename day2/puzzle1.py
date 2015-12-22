#!/usr/bin/python

"""
created by Mike Jarrett
"""

import re

f = open('input.txt','r')
dims_list = []


for line in f:
    match = re.match(r'(\d+)x(\d+)x(\d+)', line)
    dims = [ int(match.group(1)), int(match.group(2)), int(match.group(3)) ]
    dims = sorted(dims)
    dims_list.append(dims)

total_area_list = [ 2*d[0]*d[1] + 2*d[1]*d[2] + 2*d[0]*d[2] + d[0]*d[1] for d in dims_list ]


print sum(total_area_list)

