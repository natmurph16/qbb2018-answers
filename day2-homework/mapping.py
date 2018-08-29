#!/usr/bin/env python3

#Output a new file with two tab separated columns, first containg the FlyBase ID and second containing the Uniprot ID (AC)

import sys

#Use fly.txt as your first system argument
for line in open(sys.argv[1]):
    if "DROME" in line:
        fields = line.rstrip("\r\n").split()
        if fields[-1].startswith("FBgn"):
            print(fields[3], fields[2])
            
#Output file called "Map_out.txt"
#Output file with first 100 lines called "Map_out_100.txt"
