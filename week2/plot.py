#!/usr/bin/env python3

"""
Usage: make dot plot from lastz data

./plot.py <lastz data> <plot output file>
"""

import sys
import matplotlib.pyplot as plt

count = 0

plt.figure()

for value in open(sys.argv[1]):
    if "zstart1" in value:
        continue
    else:
        fields = value.split("\t")
        plt.plot([int(fields[0]), int(fields[2])], [count, count + int(fields[1])])
        
        count += int(fields[1])

plt.xlim( 0, 100000 )
plt.ylim( 0, 100000 )
plt.xlabel("Reference Position")
plt.ylabel("Contig Position")
plt.title(sys.argv[2])
plt.savefig(str(sys.argv[2]) + ".png")
plt.close()