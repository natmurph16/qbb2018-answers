#!/usr/bin/env python3

"""
Implement a script that finds matching k-mers between a single query sequence and a database of targets.
Script should output header, target start, query start, and kmer.
"""

import sys
import fasta

#The target is the database
target = fasta.FASTAReader(open(sys.argv[1]))
#The query is the sequence to align
query = fasta.FASTAReader(open(sys.argv[2]))

kmers = {}
k = int(sys.argv[3])

for header, sequence in query:
    for i in range(0, len(sequence) - k):
        kmer = sequence[i:i+k]
        if kmer not in kmers:
            kmers[kmer] = [i]
        else:
            kmers[kmer].append(i)
            
for header, sequence in target:
    for i in range(0, len(sequence) - k):
        kmer = sequence[i:i+k]
        if kmer in kmers:
            for var in kmers[kmer]:
                print(header, "\t", i, "\t", var, "\t", kmer)

