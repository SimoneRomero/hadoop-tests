#!/usr/bin/python

#mapper

# Write a MapReduce program which will display the number of hits for each different file on the Web site

#How many hits were made to the page "/assets/js/the-associates.js
 
import sys
import csv


for line in sys.stdin:
    data = line.strip().split(" ")

    query_string  = data[5:8]
    status_code = data[8]

    print "{0}\t{1}".format(query_string, status_code)
          
