#!/usr/bin/env python
"""
merge two files with multiple columns base on keys in one of the columns 
detault is 1st column and TAB ("\\t") as the separator 
"""
__version__ = '0.4'
__author__ = 'jmadzo'

import sys
import argparse

if len(sys.argv)==1: sys.exit("missing arguments\nfor help --help or -h")

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
group = parser.add_mutually_exclusive_group()
parser.add_argument('-a',action='store', dest='file_a', help='input file_a choose smaller one (loads to the memory)')
parser.add_argument('-b',action='store', dest='file_b', help='input file_b choose bigger (doesn\'t load to the memory)')
parser.add_argument('-k',action='store', dest='key_column', type=int , help='column with keys, when is the same for both files (default=1)', default=1)
parser.add_argument('-K1',action='store', dest='key_column1', type=int , help='column with keys in -a file (default=1)', default=1)
parser.add_argument('-K2',action='store', dest='key_column2', type=int , help='column with keys in -b file (default=1)', default=1)

parser.add_argument('-sep',action='store', dest='separator', type=str , help='column separator (default="TAB")', default="\t")
group.add_argument('-NA',action='store', dest='missing_value', type=str , help='missing value (default="-")', default="-")
group.add_argument('-no_overlap', action='store_true', help='drop out lines with non-overlaping values')

command_line=parser.parse_args()
file_a=command_line.file_a
file_b=command_line.file_b
k=(command_line.key_column)
k1=(command_line.key_column1)
k2=(command_line.key_column2)
sep=command_line.separator
NA=command_line.missing_value
noNA=command_line.no_overlap

# key asigment, if K1 or K2 were used, they will be assign, otherwise universak -k is used
k1 = k1-1 if k1>1 else k-1
k2 = k2-1 if k2>1 else k-1

with open(file_a, 'rU') as file_a:
    temp_a=[line.strip().split(sep) for line in file_a]
    a=dict((item[k1],item[:k1]+item[k1+1:]) for item in temp_a)

#assign lenght of column important for missing values, hack with len(a[a.keys()[0]]) would not work when number of columns varies between rows, 
#later if lenght of columns expends new missing values placeholders are add by: "a_colum_num =  len(a[key_b]) if len(a[key_b]) > a_colum_num else a_colum_num"
a_colum_num, b_column_num = len(a[a.keys()[0]]), 0

with open(file_b, 'rU') as file_b:
    for row in file_b:
        temp_row=row.strip().split(sep)
        key_b, value_b= temp_row[k2], temp_row[:k2]+temp_row[k2+1:]
        b_column_num =  len(temp_row[:k2]+temp_row[k2+1:]) if len(temp_row[:k2]+temp_row[k2+1:]) > b_column_num else b_column_num

        try:
            if key_b in a: #.keys(): 
                print("\t".join([key_b] + a[key_b] + value_b))
                a_colum_num =  len(a[key_b]) if len(a[key_b]) > a_colum_num else a_colum_num
                del a[key_b]
            elif noNA:
                continue
            else:
                print("\t".join([key_b]+ [NA]*a_colum_num + value_b))
        except Exception as err:
            raise err
            pass
if not noNA:
    for key_a in a: print("\t".join([key_a] + a[key_a]+[NA]*b_column_num))
