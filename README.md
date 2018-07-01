# RetroSpotter

* A computational pipeline for measuring the expression of Human Endogenous Retroviruses using publicly available RNA Seq Data.

## What is RetroSpotter?

The human genome has many Human Endogenous Retroviruses (HERVs) located within it. It was been proposed that HERVs play an important role in disease. There is currently an unmet need for a tool which allows the user to test for HERV expression using RNA sequencing data. RetroSpotter allows the user to compare HERV expression in two datasets (e.g. disease and control). The tool outputs a CSV file that allows downstream analysis as well as automatically generating several other informative plots.


The tools makes it possible to measure HERV expression in a large range of publicly available datasets by streaming data from the SRA. The user provides a list of SRA accessions which RetroSpotter then aligns to a reference FASTA of HERV genomes using magicblast.

We have tested RetroSpotter by comparing an AML and a Geuvadis datasets.


## Install Instructions


#### Requirements


##### Software

* python3
* magicblast (This should be in your path)
* R (rstudio)

##### Python Libraries

* biopython
* pandas
* seaborn
* jupyter

## How to use RetroSpotter?

Before running the pipeline you must collect the following:

1. A reference FASTA file containing the HER genomes you wish to align against. See viruses/reference_genomes/retroviruses.fasta for an example.
2. Two SRR accession lists to compare. These can be collected from the [SRA](https://www.ncbi.nlm.nih.gov/sra) website.

### Setup

#### Collect Code

``` git clone https://github.com/NCBI-Hackathons/RetroSpotter.git ```

``` cd RetroSpotter ```

#### Make Blast Database

RetroSpotter requires a blast database to align against. This can be created by running the following:

``` bash viruses/makeblastdb.sh  $REF_FASTA ```

Where $REF_FASTA is the location of your reference genome FASTA. This is best stored in the viruses/reference_genomes directory.


#### Run MagicBLast Alignment Jobs

There are two options for completing the alignment process. Please note that this section should be run twice - once for each SRA accession list.
Take care to give your JOBS_DIR and OUT_DIR a different name for each accession list you align.

* If you have access to a Sun Grid Engine the jobs can be submitted using the run_jobs_qsub.sh script:

``` bash viruses/run_jobs_qsub.sh $ACC_FILE $BLAST_DB $THREADS $OUT_DIR $JOBS_DIR $TEMPLATE $COMMENT ```

Where:

ACC_FILE =  The file containing the SRR accession numbers (See /viruses/accession_lists for an example)

BLAST_DB =  The Blast database

THREADS =  The number of magic blast threads to use

OUT_DIR = The directory where your results should be placed

JOBS_DIR = The directory to put the job scripts

TEMPLATE = The grid engine submit script template (e.g. viruses/templates/grid_engine_template.txt)

COMMENT = Short comment for file name e.g. control

* Alternatively use the run_jobs.sh command:

```  bash viruses/run_jobs.sh $ACC_FILE $BLAST_DB $THREADS $OUT_DIR $COMMENT```

### Analyse

For each of the results folders run the following script.

``` bash viruses/count_hits.sh $PATH_TO_RESULTS ```

The open jupyter notebook:

``` jupyter notebook ```

* navigate to create_csv notebook. Edit location of results to your folder and reference fasta. Run notebook to generate CSV and plots.

### Visualise

``` jupyter notebook ```

* navigate to make_plots notebook. Edit the names of input files e.g. results folders and fasta location. Run the notebook to generate plots.


## Pipeline

* Create blast db of fasta
* Align using magicblast
* Count alignments per virus
* Create dataframe
* Create plots

![pipeline](https://github.com/NCBI-Hackathons/RetroSpotter/blob/joseph/figs/pipelineday3.png)


## Results

### Differential Expression

The barchart below shows the difference in expression levels between an AML and Geuvadis dataset. The Geuvadis dataset consists of cells that have been immortilised using the Epstein Barr Virus (EBV). There is some evidence that this process results in increased expression of Endogenous Retroviruses [1].

![Barchart](https://github.com/NCBI-Hackathons/RetroSpotter/blob/joseph/figs/bar.png)

### Count by Sample

The plot shows the sum of the normalised count on a per sample basis. This allows the user to spot samples with unusual expression.

![sample](https://github.com/NCBI-Hackathons/RetroSpotter/blob/master/figs/count_by_sample.png)

### Count by Sequence

The expression for a particular viral sequence. Compare between two datasets.

![counts](figs/average_expression_by_seq.png)

### PCA

A Principle Component Analsysis (PCA) of the data. Clusters within the dataset are visible.

![pca](https://github.com/NCBI-Hackathons/RetroSpotter/blob/master/figs/pca3d.png)

### Heatmap

A clustered heatmap. Samples with unusual HER expression are visible.

![pca](https://github.com/NCBI-Hackathons/RetroSpotter/blob/master/figs/heatmap.png)


## Further Work

* Run again with better control set.
* Improve HERV Reference genome! Currently some strains in there that doesn't fit well.
* Complete pipeline automation so that the results are reproducible.
* Link up with metadata from SRA.


## People/Team

* Olaitan I. Awe (Programmer, Writer and Project Maintainer)

* Joseph Halstead (Team Lead and Programmer)

* Ian Taukulis (Programmer)

* Jozef Madzo (Sys Admin and Programmer)

* Xiaoyu Zhai (Writer and Programmer)

* Ben Busby (Resources)

## References

[1] http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0044991
