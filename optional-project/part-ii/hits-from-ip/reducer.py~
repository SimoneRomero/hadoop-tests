#!/usr/bin/python


## reducer

# Write a MapReduce program which will display the number of hits for each different file on the Web site

# How many hits were made to the page "/assets/js/the-associates.js

import sys

countHit = 0
for line in sys.stdin:
    data = line.strip().split('\t')
    
    if len(data) != 2:
        continue

    query, status = data
    link = query.split(" ")

    if "/assets/js/the-associates.js" in link[1]:
        countHit += 1

print "{0}".format(countHit)
