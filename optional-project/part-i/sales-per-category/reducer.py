#!/usr/bin/python


## reducer- Sales per Category

# Format of each line is:
# "date" "time" "store-name" "item-description" "cost" "method-of-payment"

# Instead of breaking the sales down by store, give us a sales breakdown by product category across all of our stores.

import sys

oldKey = None
totalSales = 0

for line in sys.stdin:
    data = line.strip().split('\t')
    
    if len(data) != 2:
        continue

    currentKey, cost = data

    if oldKey and oldKey != currentKey:
        print "{0}\t{1}".format(oldKey, totalSales)

        totalSales = 0
    
        

    oldKey = currentKey
    totalSales += float(cost)


if oldKey != None:
   print "{0}\t{1}".format(oldKey, totalSales)
