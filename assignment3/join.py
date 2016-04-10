# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 14:16:15 2015

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
    key = record[1]
    value = record
    mr.emit_intermediate(record[1],record)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    ordrs = []
    items = []
    # total = 0
    for v in list_of_values:
        # total += v
        if v[0] == 'line_item':
            items.append(v)
        else:
            ordrs.append(v)
    # mr.emit((key, total))
    for order in ordrs:
        for item in items:
            if order[1] == item[1]:
                mr.emit((order + item))

# Part 4
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)