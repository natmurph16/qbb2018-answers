#!/usr/bin/env python3

#Find the nearest non-protein-coding gene to 3R:21,378,950 for Drosophila

import sys

find_pos = 21378950

genes_dict = {}


for line in open(sys.argv[1]):
    #Skip the header, which all begins with "#"
    if "#" in line:
        continue
    #Split the columns based on tab
    fields = line.rstrip("\r\n").split("\t")
    #If column 3 specifies "gene", then
    if fields[2].startswith("gene") and fields[0] == "3R":
        gene_start = int(fields[3])
        gene_end = int(fields[4])
        info = fields[8].split()
        my_dist = 0
        if "gene_id" in info:
            gene_id_index = info.index("gene_id")
            gene_name_index = gene_id_index + 1
        if "gene_biotype" in info:
            bio_type_index = info.index("gene_biotype")
            gene_type_index = bio_type_index + 1
            if info[gene_type_index] != '"protein_coding";':
                if find_pos < gene_start:
                    my_dist = gene_start - find_pos
                    genes_dict[my_dist] = info[gene_name_index]
                elif find_pos > gene_end:
                    my_dist = find_pos - gene_end
                    genes_dict[my_dist] = info[gene_name_index]                    

keys_list = genes_dict.keys()
dist_min = min(keys_list)
print("Nearest non-protein-coding gene:", genes_dict[dist_min])

#Output saved as near_gene_noncoding



    
