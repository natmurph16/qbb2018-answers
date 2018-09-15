#!/usr/bin/env python3

"""
Usage: Write a python script to compute the number of contigs,
minimum/maximum/average contig length, and N50

./contig_counter.py <velvet.fa file> <spades.fa file>
"""


import sys
import numpy as np
import matplotlib.pyplot as plt
import fasta

velvet_contigs = fasta.FASTAReader(open(sys.argv[1]))

def do_stats(fasta_file):
    num_contig = 0
    length_contig = []

    for (header, sequence) in fasta_file:
        num_contig += 1
        length_contig.append(len(sequence))

    length_contig.sort(reverse = True)
    print(num_contig)
    print(length_contig)
    print("Min contig length:" + str(sum(length_contig)/num_contig))
    print("Max contig length:" + str(length_contig[0]))
    print("Avg contig length:" + str(length_contig[-1]))
    
    length_half = sum(length_contig)/2
    counter = 0
    for length in length_contig:
        if counter <= length_half:
            counter += length
        else:
            print("n50:" + str(length))
            break
    
    
do_stats(velvet_contigs)
    
#print(length_seq)





