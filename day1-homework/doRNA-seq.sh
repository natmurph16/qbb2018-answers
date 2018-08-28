#!/bin/bash

GENOME=~/qbb2018-answers/genomes/BDGP6
ANNOTATION=~/qbb2018-answers/genomes/BDGP6.Ensembl.81.gtf

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
  mkdir $SAMPLE
  cd $SAMPLE
  echo "Running fastqc"
  fastqc ~/data/rawdata/${SAMPLE}.fastq
  echo "Running hisat2"
  hisat2 -x $GENOME -U ~/data/rawdata/${SAMPLE}.fastq -S ${SAMPLE}_map.sam
  echo "Running samtools"
  samtools sort -o ${SAMPLE}_map.bam ${SAMPLE}_map.sam
  samtools index -b ${SAMPLE}_map.bam
  echo "Running stringtie"
  stringtie ${SAMPLE}_map.bam -p -e -G $ANNOTATION -B -o ${SAMPLE}_pot.gtf
  cd ../
done
