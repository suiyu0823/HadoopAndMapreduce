#!/usr/bin/python

import sys

nodeIds = ""
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, nodeId = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", nodeIds
        oldKey = thisKey
        nodeIds = ""

    oldKey = thisKey
    nodeIds += nodeId+","

if oldKey != None:
    print oldKey, "\t", nodeIds
