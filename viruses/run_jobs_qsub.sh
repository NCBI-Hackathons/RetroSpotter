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
fi


if [ -z "$5" ]
  then
    echo "No argument supplied"
    exit 1
fi

if [ -z "$6" ]
  then
    echo "No argument supplied"
    exit 1
fi

if [ -z "$7" ]
  then
    echo "No argument supplied"
    exit 1
fi


ACC_FILE=$1 #File containg SRR accession numbers
BLAST_DB=$2 #Blast database
THREADS=$3 #Number of magic blast threads to use
OUT_DIR=$4 #Where to put the results when job in run
JOBS_DIR=$5 #Where to put the jobs
TEMPLATE=$6 #The grid engine submit script template
COMMENT=$7 #Short comment for file name

# clear and create jobs folder
rm -r $JOBS_DIR/
mkdir $JOBS_DIR/

rm -r $OUT_DIR/
mkdir $OUT_DIR/

# make the jobs
for i in $( cat $ACC_FILE ); do

  cp $TEMPLATE $JOBS_DIR/job_$i.sh
  echo "magicblast -db $BLAST_DB -sra $i -no_unaligned -num_threads $THREADS -out $OUT_DIR/$COMMENT.$i.sam" >> $JOBS_DIR/job_$i.sh

done

# run those jobs

for i in $JOBS_DIR/*.sh; do

  sleep 0.1 #So that the reciever doesn't get overwhelmed
  echo "submitting job $i"
  echo qsub $i
  echo "----------------"

done
