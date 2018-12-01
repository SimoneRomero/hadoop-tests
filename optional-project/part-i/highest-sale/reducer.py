#!/usr/bin/python


## reducer - Highest Sale

# Find the monetary value for the highest individual sale for each separate store.

import sys

oldLocal = None
highestValue = 0

for line in sys.stdin:
    data = line.strip().split('\t')
    
    if len(data) != 2:
        continue

    currentLocal = data[0]
    currentValue = float(data[1])

    if oldLocal and oldLocal != currentLocal:
        print "{0}\t{1}".format(oldLocal, highestValue)
        highestValue = 0
    
        
    oldLocal = currentLocal
    if currentValue > highestValue:
        highestValue = currentValue
        



if oldLocal != None:
   print "{0}\t{1}".format(oldLocal, highestValue)
