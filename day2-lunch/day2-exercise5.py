#!/usr/bin/env python3

import sys
import statistics

if len(sys.argv) > 1:
    f = open( sys.argv[1] )
else:
    f = sys.stdin
        
count = 0
score = 0

for i, line in enumerate( f ):
    if line[0] == "@":
        continue
    count += 1
    fields = line.strip().split("\t")
    score += int(fields[4])

average = float(score / count)

print(average)