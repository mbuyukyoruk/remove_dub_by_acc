import argparse
import os
import re
import sys
import textwrap
import uuid

parser = argparse.ArgumentParser(prog='python remove_dub_by_acc.py',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('''\
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

      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename',
                    help='Specify a original fastafile with duplicate accessions.\n')

parser.add_argument('-o', '--output', required=True, dest='out',
                    help='Specify a output fastafile name.\n')

results = parser.parse_args()
filename = results.filename
out = results.out

os.system('> ' + out)

temp = 'temp_' + str(uuid.uuid4().hex) + '.txt'

os.system("""awk 'BEGIN{RS=">"}NR>1{sub("\\n","\\t"); gsub("\\n",""); print RS$0}' """ + filename + """ | awk '!seen[$1]++' > """ + temp)

with open(temp, 'r') as file:
    for line in file:
        if line[0] == '>':
            arr = line.split('\t')
            f = open(out, 'a')
            sys.stdout = f
            print(arr[0])
            print(re.sub("(.{60})", "\\1\n", str(arr[1].split('\n')[0]), 0, re.DOTALL))

os.system('rm ' + temp)