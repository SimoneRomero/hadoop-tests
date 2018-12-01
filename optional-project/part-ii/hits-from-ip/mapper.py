#!/usr/bin/python

#mapper

# Write a MapReduce program which determines the number of hits to the site made by each different IP address

#How many hits were made by the IP address 10.99.99.186?
 
import sys
import csv


for line in sys.stdin:
    data = line.strip().split(" ")

    ip  = data[0]
    print "{0}".format(ip)
    
          
