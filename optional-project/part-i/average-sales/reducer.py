#!/usr/bin/python


## reducer
#Write a mapreduce program that processes the purchases.txt file and outputs mean (average) of sales for each weekday. 

import sys

oldKey = None
totalSales = 0
count = 0


for line in sys.stdin:
    data = line.strip().split('\t')
    
    if len(data) != 2:
        continue

    currentKey, cost = data

    if oldKey and oldKey != currentKey:
        mean = float(totalSales)/float(count)
        print "{0}\t{1}\t{2}\t{3}".format(oldKey, totalSales, count, mean)

        totalSales = 0
        count = 0
        

    oldKey = currentKey
    totalSales += float(cost)
    count += 1

if oldKey != None:
   mean = float(totalSales)/float(count)
   print "{0}\t{1}\t{2}\t{3}".format(oldKey, totalSales, count, mean)
