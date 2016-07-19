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

    tagsWithCountValue = []
   
    oldTag = None
    count = 0
    for line in reader:
        if len(line) != 2:
             continue
    
        thisTag, thisNumber = line
         
        if oldTag and oldTag != thisTag:
            tagsWithCountValue.append([count, oldTag])
            oldTag = thisTag
            count = 0

        oldTag = thisTag
        count += 1  

    if oldTag != None:
        tagsWithCountValue.append([count, oldTag])

    tagsWithCountValue.sort()
    tagsWithCountValue.reverse()

    for line in tagsWithCountValue[:10]:
        writer.writerow([line[1], line[0]])     

if __name__ == "__main__":
    reducer()
