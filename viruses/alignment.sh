#!/bin/bash

if [ -z "$1" ]
  then
    echo "No argument supplied"
    exit 1
fi

if [ -z "$2" ]
  then
    echo "No argument supplied"
    exit 1
fi


if [ -z "$3" ]
  then
    echo "No argument supplied"
    exit 1
fi

if [ -z "$4" ]
  then
    echo "No argument supplied"
    exit 1


if [ -z "$5" ]
  then
    echo "No argument supplied"
    exit 1
fi




ACC_FILE=$1 #File containg SRR accession numbers
BLAST_DB=$2 #Blast database
THREADS=$3 #Number of magic blast threads to use
OUT_DIR=$4 #Where to put the results when job in run
COMMENT=$5 #Short comment for file name

# clear and create jobs folder
rm -rf $JOBS_DIR/
mkdir $JOBS_DIR/

for i in $( cat $ACC_FILE ); do

  echo $i

  sem -j +0 ../../../applications/ncbi-magicblast-1.3.0/bin/magicblast -db $BLAST_DB -sra $i -no_unaligned -num_threads $THREADS -out $OUT_DIR/$COMMENT.$i.sam 

done

sem --wait





