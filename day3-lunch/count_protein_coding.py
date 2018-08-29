#!/usr/bin/env python3

#Count the number of protein coding genes for Drosophila

import sys

count = 0

for line in open(sys.argv[1]):
    #Skip the header, which all begins with "#"
    if "#" in line:
        continue
    #Split the columns based on tab
    fields = line.rstrip("\r\n").split("\t")
    #If column 3 specifies "gene", then
    if fields[2].startswith("gene"):
        info = fields[8].split()
        if "gene_biotype" and '"protein_coding";' in info:
            count += 1
print(count)

#Output saved as num_protein_coding