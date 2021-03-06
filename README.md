# ncbifetcher

#### Hello there
This program is designed to be a user friendly storage space for mitochondrial genomes, elements, genes, and protein outputs. The program has integration for ncbi through biopython while also the user has an option to import their own sequences, genomes, etc to all be integrated. The program also has keeps records of what is stored in storage. With these records, another module can pull what is specified from these records (indexes) and consolidate them into a fasta file. Mafft is supported so the outputed files can then be aligned as another output.

If there are any questions, concerns, or nice stories; please don't hesitate to contact at wwinnett@iastate.edu.

This project was made in conjunction with Lavrov lab and under the supervision of Dr. Muthye and Dr. Lavrov.

### Instructions:
There are a couple of things that you can do with this project:
1) Download genbank (.gb), genomes(.fa), and genes (.fa) to the base storage file (default is in project directory). You can do this by running from **fetcher.py**:

```
battery(query, output location)
```

Query can be treated as if you were searching ncbi by itself. So things like accession numbers, taxonomy (such as txid2754381[Organism]), or boolean operators (mouse AND mitochondria). Running this also updates the indexes (gene.lst and species.lst).

2) The genes can be pulled from storage and consolidated into a new fasta file containing all of the genes from a species and from a gene. To specify which genes and/or species, uncomment the genes or species you want from the index. 

```
Selected: ATP6,
Unselected or commented out: ;ATP6.
```

By default, the comment is a semi-colon. The indexes location is also under the indexes folder in the project directory. The outputs are fastas and the clustal aligned files. 

To run this feature, run the **puller.py**

### Road map 
- Parse the gene bank and download raw data
- Save the raw data to a .gb file
- Create a fasta out of the individual pieces to it (as .fa)
- Create an amino acid version of the fasta (as .faa)
- Create a fasta out of the whole genome (full\_fa/*.fa)
- Create an amino acid fasta out of the whole genome (full_faa/*.faa)
- Create a battery that does all three processes

##### Indexer
- Save the storage as an smooth and easy way to work with the saved files
- Automate refreshing and resetting of indexes

##### Puller
- Neatly pull out desired information as directed by the indexes. Save them as a fasta
- Align the fasta and save as a clustal aligned file (.aln)

#### TODO
- [ ] Allow for the storage and output to have easy integration
- [ ] Allow the program to be called from the command line
- [ ] Implement an algorithm for output of puller
- [ ] Allow translation to be specified by the genbank file rather than default
- [ ] Allow the user to specify an optional parameters to the argument.

###### Late game TODO 
- [ ] Integrate R shiny
- [ ] Provide windows support for mafft

#### Known issues
- [x] Translating of sequence is not being called.
