#!/usr/bin/python

import sys

oldKey = None
topFile = None
hits = 0
maxHits = 0
ind = -1

for line in sys.stdin:
  data_mapped = line.strip().split()
  if len(data_mapped) != 1:
    continue
    
  key = data_mapped
  thisKey = key
  
  if not key:
    continue
    
  if oldKey and oldKey != thisKey and thisKey not in oldKey:
    if hits > maxHits:
      maxHits = hits
      topFile = oldKey
    oldkey = thisKey
    hits = 0
    
  oldKey = thisKey
  hits += 1
  
print topFile, "\t", maxHits
