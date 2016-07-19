#!/usr/bin/python

import sys

for line in sys.stdin:
    content = line.strip().split(",")
    print len(content)
