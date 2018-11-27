#!/usr/bin/python

#mapper

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
#Write a mapreduce program that processes the purchases.txt file and outputs mean (average) of sales for each weekday. 


import sys
import csv
from datetime import datetime


for line in sys.stdin:
    data = line.strip().split("\t")
    print len(data)
    print "tamanho"

    day  = data[0]
    value = data[4]
    weekday = datetime.strptime(day, "%Y-%m-%d").weekday()
    print "{0}\t{1}".format(weekday, value)
      
