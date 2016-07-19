#!/usr/bin/python

import sys

count = 0
mostCount = 0
oldAuthor = None
mostHour = None
oldHour = None


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisAuthor, thisHour = data_mapped
     
    if oldAuthor and oldAuthor != thisAuthor:
        if count >= mostCount:
            mostCount = count
            mostHour = oldHour 

        print oldAuthor, "\t", mostHour

        oldAuthor = thisAuthor
        oldHour = thisHour
        count = 0
        mostCount = 0
        mostHour = None

    #when a different hour is scanned
    if oldHour and oldHour != thisHour:
        if count >= mostCount:
            mostCount = count
            mostHour = oldHour 
        oldHour = thisHour
        count = 0

    #when the hour is first scanned or a same hour is scanned
    oldHour = thisHour
    count += 1

    #when the author is first scanned or a same author is scanned
    oldAuthor = thisAuthor

if oldAuthor != None:
    if count >= mostCount:
        mostCount = count
        mostAuthor = oldAuthor
 
    print oldAuthor, "\t", mostHour

