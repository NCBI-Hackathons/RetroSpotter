#!/bin/bash

REF_FASTA=$1

mkdir blast_dbs

makeblastdb -in $REF_FASTA  -dbtype nucl -parse_seqids -out viruses/blast_dbs/referencedb
