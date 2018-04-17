#!/bin/bash

# A quick script for submitting jobs to Grid Engine

if [ -z "$1" ]
  then
    echo "No jobs folder argument supplied"
    exit 1
fi

JOBS_FOLDER=$1 # folder with jobs in

for i in $JOBS_FOLDER/*.sh; do

  sleep 0.1 #So that the reciever doesn't get overwhelmed
  echo "submitting job $i"
  qsub $i
  echo "----------------"

done