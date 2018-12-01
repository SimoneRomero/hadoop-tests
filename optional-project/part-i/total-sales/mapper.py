#!/usr/bin/python

#mapper- Total Sales

# Find the total sales value across all the stores, and the total number of sales. 

import sys
import csv

for line in sys.stdin:
    data = line.strip().split("\t")

    value = data[4]
    print "{0}".format(value)
      
