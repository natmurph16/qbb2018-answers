#!/usr/bin/env python3

"""
Usage: Use BLAST to identify homologous sequences to your query of interest
"""



import sys
import fasta

#The DNA_seq is the blast output file
DNA_seq = fasta.FASTAReader(open(sys.argv[1]))
#The AA_seq is the MAFFT output file
AA_seq = fasta.FASTAReader(open(sys.argv[2]))


for (dna_id, dna), (aa_id, aa) in zip(DNA_seq, AA_seq):
    new_dna = ""
    j=0
    for i in range(len(aa)):
        a = aa[i]
        nuc = dna[j:j+3]
        if a == "-":
            new_dna += "---"
        else:
            new_dna += nuc
            j +=3
    print(dna_id + "\n" + new_dna)

#output piped to "homologous"



    # seq_dna = []
    # seq_aa = []
    #
    # for (dna_id, dna), (aa_id, aa) in zip(DNA_seq, AA_seq):
    #     new_dna = ""
    #     j=0
    #     for i in range(len(aa)):
    #         a = aa[i]
    #         seq_aa.append(a)
    #         nuc = dna[j:j+3]
    #         if a == "-":
    #             seq_dna.append("---")
    #         else:
    #             seq_dna.append(nuc)
    #             j +=3
    #
    # #print(seq_dna)
    # print(seq_aa)
    

