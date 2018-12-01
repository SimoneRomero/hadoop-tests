#!/usr/bin/python


## reducer - Total Sales

# Find the total sales value across all the stores, and the total number of sales. 

import sys

totalSales = 0
count = 0

for line in sys.stdin:    

    value =float(line)
    count += 1 
    totalSales += value 

print "{0}\t{1}".format(count, totalSales)
