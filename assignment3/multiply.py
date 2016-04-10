# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 00:23:12 2015

@author: Dat Tien Hoang
"""

import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = (record[1], record[2], record[3])
    if key == 'a':
        for i in range(5):
            mr.emit_intermediate((value[0], i), ('a', value[1], value[2]))
    if key == 'b':
        for i in range(5):
            mr.emit_intermediate((i, value[1]), ('b', value[0], value[2]))
    # mr.emit_intermediate((value,key),1)

# Part 3
def reducer(key, list_of_values):
    a_vals = []
    b_vals = []
    for v in list_of_values:
        if v[0] == 'a':
            a_vals.append(v)
        if v[0] == 'b':
            b_vals.append(v)
    tot = 0
    for p in a_vals:
        for q in b_vals:
            prod = 0
            if p[1] == q[1]:
                prod = p[2] * q[2]
                tot += prod
    mr.emit((key[0], key[1], tot))

# Part 4
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)