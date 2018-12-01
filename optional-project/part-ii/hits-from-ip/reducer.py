#!/usr/bin/python


## reducer

# Write a MapReduce program which will display the number of hits to the site made by each different ip address

# how many hits were made by the IP address 10.99.99.186?

import sys

oldIp = None
count = 0

for line in sys.stdin:
    ip = line
    
    if oldIp and oldIp != ip:
        print oldIp, "\t", count
        count = 0
        oldIp = ip

    oldIp = ip
    count += 1


if oldIp != None:
    print "{0}\t{1}".format(oldIp, count)
    
