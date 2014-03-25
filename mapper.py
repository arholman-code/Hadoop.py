#!/usr/bin/python

# Format of each line is :
# ip address\id of client\username\datetime\timezone\command\uri\req\status\size
#
# Only need 1 element - uri/path
# We need to write to standard output for reducing

import sys

for line in sys.stdin:
  data = line.strip().split()
  if len(data) == 10:
    print "{0}".format(data[6])
