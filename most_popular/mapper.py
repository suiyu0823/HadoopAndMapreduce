#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, identity, username, time, timezone, method, path, protocol, status, size = data
        fileName = path.split('/')[-1]
        query = re.sub('http://www.the-associates.co.uk','', path)
        print "{0}\t{1}".format(query, fileName)

