# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:28:30 2015

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
    words = value.split()
    for w in words:
        # mr.emit_intermediate(w, 1)
        mr.emit_intermediate(w,record[0])

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    invind = []
    # total = 0
    for v in list_of_values:
        # total += v
        if v not in invind:
            invind.append(v)
    # mr.emit((key, total))
    mr.emit((key, invind))

# Part 4
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)