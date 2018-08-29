#!/usr/bin/env python3

#Count the number of "types of genes" for Drosophila

import sys

biotype_dict = {}

for line in open(sys.argv[1]):
    #Skip the header, which all begins with "#"
    if "#" in line:
        continue
    #Split the columns based on tab
    fields = line.rstrip("\r\n").split("\t")
    #If column 3 specifies "gene", then
    if fields[2].startswith("gene"):
        info = fields[8].split()
        if "gene_biotype" in info:
            bio_type_index = info.index("gene_biotype")
            gene_type_index = bio_type_index + 1
            if info[gene_type_index] in biotype_dict:
                biotype_dict[info[gene_type_index]] += 1
            else:
                biotype_dict[info[gene_type_index]] = 1
                
for name, value in biotype_dict.items():
    print(name, value)
    
#Output saved as num_gene_types