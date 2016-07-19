#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()

for data in reader:
    if len(data) == 19:
        hour = int(data[8][11:13])
        author_id = data[3]
        print "{0}\t{1}".format(author_id, hour)

