#!/usr/bin/python

#mapper - Sales per Category

# Format of each line is:
# "date" "time" "store-name" "item-description" "cost" "method-of-payment"

# Instead of breaking the sales down by store, give us a sales breakdown by product category across all of our stores.

import sys
import csv


for line in sys.stdin:
    data = line.strip().split("\t")
    
    category  = data[3]
    cost = data[4]

    print "{0}\t{1}".format(category, cost)
      
