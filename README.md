# Differential Expression of Copy Number Variation (CNVS) from RNA Seq

* Finding gene duplications in RNA Seq is not normally possible. However sometimes a specific duplication is associated with particular SNPs.

* We can look for these SNPs in RNA Seq data and therefore find the duplications.


## What's the problem ?


* Copy Number Variations (CNVs) are the cause of a number of human disease. Any tool which aids the discovery of CNVs would be of great use.


* How do we find the SNPS associated with duplications and CNVs? There are 3 options:

	1) Possible we can use dbDNV - a database of SNPs associated with gene duplications.
	2) Try looking at 1000 genome data - to do.
	3) Curated SNPs e.g. Tryptase locus.


## What is INSERT NAME ?



## How to use INSERT NAME ?

How to run the software

### Install Instructions


#### Requirements


##### Software

* python3
* magicblast

##### Python Libraries

* pysam
* bipython

### Running the application


## Pipeline

* Use SNPs and RNA Seq data to find possible duplications.

* Input: data from SRA and gene name

* Output: Diffential expression plots

### Day 1

![alt text](https://github.com/NCBI-Hackathons/SVRNA/blob/master/figs/pipeline.png)

### Day 2

![alt text](https://github.com/NCBI-Hackathons/SVRNA/blob/joseph/figs/pipeline2.png)

## People/Team

Ian Taukulis

Jozef Madzo

Xiaoyu Zhai

Joseph Halstead

## References


* https://www.ncbi.nlm.nih.gov/pmc/articles/pmid/21097891/


