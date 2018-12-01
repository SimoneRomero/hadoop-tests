#!/usr/bin/python

#mapper - Highest Sale

# Find the monetary value for the highest individual sale for each separate store.

import sys
import csv


for line in sys.stdin:
    data = line.strip().split("\t")
    
    local  = data[2]
    cost = data[4]

    print "{0}\t{1}".format(local, cost)
      
