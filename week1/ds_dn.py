#!/usr/bin/env python3

"""
Usage: Compile the number of dS and dN mutations between first hit and all others
"""

import sys
import numpy as np
import matplotlib.pyplot as plt


new_align = open(sys.argv[1])


dictionary = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }


def codon_splitter(sequence, k):
    return [sequence[i:i+k] for i in range(0, len(sequence), k)]


new_align.readline()
first_line = codon_splitter(new_align.readline(), 3)

dS = np.zeros(len(first_line))
dN = np.zeros(len(first_line))

for line in new_align:
    if line[:2] == "gi":
        continue
    for index, (codon, ref) in enumerate(zip(codon_splitter(line, 3), first_line)):
        if codon == ref:
            continue
        if not codon in dictionary or not ref in dictionary:
            continue
        if dictionary[codon] == dictionary[ref]:
            dS[index] += 1
        else:
            dN[index] += 1
            
           
diff_list = dN - dS

for i in range(len(first_line)):
    if dS[i] > 0:
        print("{}\t{}\t{}".format(first_line[i], float(dN[i])/dS[i], diff_list[i]))
        

#output file piped to "mut_type"
 