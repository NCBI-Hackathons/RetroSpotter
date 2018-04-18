#!/usr/bin/env python

import sys

try:
    rsNumber = {line.strip() for line in open(sys.argv[1])}

    with open(sys.argv[2],"r") as geno_file:
        for line in geno_file:
            item = line.strip().split('\t')
            try:
                if item[2] in rsNumber:
                    print(line, end="");
            except:
                pass
except:
    sys.exit("no file provided\nneeds two files: file with rs_number and vcf file")