#!/bin/bash

grep -v "^@" ~/qbb2018-answers/day1-homework/SRR072893/SRR072893_map.sam | grep -v 2110000 > SRR072893_trim.bam
cut -f 3 SRR072893_trim.bam | sort | uniq -c > SRR072893_align_num.bam
