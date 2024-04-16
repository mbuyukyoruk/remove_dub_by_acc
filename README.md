# remove_dub_by_acc

Author: Murat Buyukyoruk

        remove_dub_by_acc help:

This script is developed to remove duplicated sequences from a multi fasta file by using Accession number. (Note: if you want to remove sequences with sequence similarity, please use cdhit tool instead.) 

When do you need this?
In cases you are downloading genome sequences from NCBI RefSeq and Genbank databases together, occasionally you will end up with two entires for the same accession. This script makes it easy to manipulate a long multifasta file.

Syntax:

        python remove_dub_by_acc.py -i demo_with_dub.fasta -o demo_removed_dubs.fasta

Input Paramaters (REQUIRED):
----------------------------
	-i/--input		FASTA			Specify a input fasta file contains duplicated accessions.

	-o/--output		FASTA			Specify a output fasta file name for non-duplicate version.

Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.

