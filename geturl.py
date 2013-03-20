#!/usr/bin/python
import urllib2
import sys

SEARCH_STRING = "position = puppetdb-intern"

if len(sys.argv) != 3:
    print "Usage: geturl.py <url> <filepath>"
    exit(1)
url = sys.argv[1]
filepath = sys.argv[2]
urldata = urllib2.urlopen(url)

with open(filepath, 'w') as f:
    for line in urldata:
        f.write(line)

with open(filepath, 'r+') as f:
    matchFound = False
    for line in f:
        if SEARCH_STRING in line:
            matchFound = True
            break
    if not matchFound:
        f.write(SEARCH_STRING + "\n")

