# RetroSpotter

* A computational pipeline for measuring the expression of Endogenous Retroviruses using publically available RNA Seq Data.


## What is RetroSpotter?

The human genome has many Human Endogenous Retroviruses (HERs) located within it. It was been proposed that HERs play a role in disease. There is currently an unmet need for a tool that will allow the user to test for HER expression using RNA sequencing data. RetroSpotter allows the user to compare HER expression in two datasets (e.g. diseease and control). The tool outputs a CSV file that allows downstream analysis as well as automatically generating several informative plots.


We have tested RetroSpotter comparing AML and a Geuvadis dataset.


### Install Instructions


#### Requirements


##### Software

* python3
* magicblast
* R

##### Python Libraries

* pysam
* biopython
* pandas
* seaborn

## How to use RetroSpotter?

### Setup

``` git clone https://github.com/NCBI-Hackathons/RetroSpotter.git ```

``` cd viruses ```

``` mkdir results ```

### Run magicblast alignments

```  bash alignment.sh $accession_list_file $blast_database $num_cores $results_directory $comment ```

### Analyse

``` bash count_hits.sh $PATH_TO_RESULTS ``` 

``` jupyter notebook ```

* navigate to create_csv notebook. Edit location of results to your folder. Run notebook to generate CSV and plots.

### Visualise

* Coming soon!

## Pipeline

* Create blast db of fasta
* Align using magicblast
* Count alignments per virus
* Create dataframe
* Create plots

![pipeline](https://github.com/NCBI-Hackathons/RetroSpotter/blob/joseph/figs/pipelineday3.png)


## Results

The barchart below shows the difference in expression levels between an AML and Geuvadis dataset. The Geuvadis dataset consists of cells that have been immortilised using the Epstein Barr Virus (EBV). There is some evidence that this process results in increased expression of Endogenous Retroviruses [1]. 

![Barchart](https://github.com/NCBI-Hackathons/RetroSpotter/blob/joseph/figs/bar.png)


## Further Work

* Run again with better different controls set.
* Complete pipeline automation so that the results are reproducible.
* Link up with metadata from SRA.
* Improve reference sequence FASTA. Automate the collection of this.


## People/Team

* Ian Taukulis

* Joseph Halstead

* Jozef Madzo

* Xiaoyu Zhai



## References

[1] http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0044991
