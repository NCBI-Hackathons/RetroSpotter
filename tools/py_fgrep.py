#!/usr/bin/env python
"""
when you try to grep the list of entries from big file >50 GB 
grep use up too much virtual memmory and eventually crash...

run py_fgerp.py column file bigFile   

"""

import sys

try:
    column = sys.argv[1]-1
    rsNumber = {line.strip() for line in open(sys.argv[2])}

    with open(sys.argv[column],"r") as geno_file:
        for line in geno_file:
            item = line.strip().split('\t')
            try:
                if item[2] in rsNumber:
                    print(line, end="");
            except:
                pass
except:
    sys.exit("no file provided\n\nneeds two files: file with rs_number and vcf file\n\n" + __doc__)