#!/usr/bin/env python3

"""
Usage: parse the phenotype file to proper plink input format

./parse.py <phenotype file>
"""

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

f = open(sys.argv[1])

for line in f:
    if "Cadmium" in line:
        print(line)
    else:
        newline = line.replace("_", "\t")
        print(newline)
        
#pipe to new file in command line