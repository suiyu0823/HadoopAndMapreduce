#!/usr/bin/python

import sys

count = 0
oldFile = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    thisFile = data_mapped

    if oldFile and oldFile != thisFile:
        print oldFile, "\t", count
        oldFile = thisFile;
        count = 0

    oldFile = thisFile
    count += 1

if oldFile != None:
    print oldFile, "\t", count

