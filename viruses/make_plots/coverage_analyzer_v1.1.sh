#!/bin/bash
#For an analysis of all the phages in sample sequence: 
echo "Here is the analysis of all phages in each sample:"
for f in `ls *.bedgraph`; do
echo ""
echo $f
echo "---"
awk -F\t 'NR>1{if ($4 < 3) {arrlow[$1]++} else {arrhi[$1]++}} END {for (a in arrlow) { if(length(arrlow[a]) == 0){arrlow[a] = 0} if(length(arrhi[a]) == 0){arrhi[a] = 0} print a, 100*(arrhi[a])/(arrlow[a] + arrhi[a]),"%" }}' $f; done