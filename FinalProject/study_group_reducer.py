#!/usr/bin/python
"""
We are interested to see if there is a correlation between the length of a post
and the length of answers.
Write a mapreduce program that would process the forum_node data and output the
length of the post and the average answer (just answer, not comment) length for
each post. You will have to decide how to write both the mapper and the reducer
to get the required result.
"""

import sys
import csv

def reducer():
    """
    MapReduce Reducer.
    """
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = \
        csv.writer(
            sys.stdout, delimiter='\t')

    oldKey = None
    id = []

    for line in reader:
        if len(line) != 2:
             continue
    
        thisKey, thisId = line
         
        if oldKey and oldKey != thisKey:
             writer.writerow([oldKey, id])
             oldKey = thisKey
             id = []

        oldKey = thisKey
        id += [thisId]  

    if oldKey != None:
        writer.writerow([oldKey, id])

if __name__ == "__main__":
    reducer()
