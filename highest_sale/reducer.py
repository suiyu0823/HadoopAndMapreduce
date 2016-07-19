#!/usr/bin/python

import sys

list1 = []
list2 = []
list3 = []

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    thisSale = float(thisSale)
    if thisKey == "Reno":
        list1.append(thisSale)
    if thisKey == "Toledo":
        list2.append(thisSale)
    if thisKey == "Chandler":
        list3.append(thisSale)

print "Reno", "\t", max(list1)
print "Toledo", "\t", max(list2)
print "Chandler", "\t", max(list3)


