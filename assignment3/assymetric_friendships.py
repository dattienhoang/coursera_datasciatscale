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
    key = record[0]
    value = record[1]
    mr.emit_intermediate((key,value),1)
    mr.emit_intermediate((value,key),1)

# Part 3
def reducer(key, list_of_values):
    if len(list_of_values) == 1:
        mr.emit((key))

# Part 4
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
