# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 00:02:29 2015

@author: Dat Tien Hoang
"""

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
    mr.emit_intermediate(key,value)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    counter = 0
    # total = 0
    for v in list_of_values:
        # total += v
        counter += counter + 1
    mr.emit((key, counter))

# Part 4
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)