#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2018-11-16
Purpose: Get fields from a tab/csv file
"""

import csv
import argparse
import os
from Bio import SeqIO
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'blasthits', metavar='FILE', help='BLAST output (-outfmt 6)')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotation file',
        metavar='FILE',
        type=str,
        default='')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    args = get_args()
    blast_hits = args.blasthits
    out_file = args.outfile
    annotation_file = args.annotations


    if not os.path.isfile(blast_hits):
        die('"{}" is not a file'.format(blast_hits))
    if not os.path.isfile(annotation_file):
        die('"{}" is not a file'.format(annotation_file))

    #create 2 dicts of key = sequence_id and value = genus or species
    species = {}
    genus = {}
    with open(annotation_file, 'rU') as annotation_file_fh:
        annotations = csv.DictReader(annotation_file_fh)
        for row in annotations:
            #if row['genus'] == '':
                #print('rowgenus is empty')
            #    genus[row['centroid']] = 'NA'
            #else:
            genus[row['centroid']] = row['genus']
            species[row['centroid']] = row['species']

    with open(blast_hits, 'r') as blast_hits_fh:
        blast_result = csv.DictReader(blast_hits_fh, fieldnames=['qseqid', 'sseqid', 'pident', \
            'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore'], delimiter='\t')

        if not out_file:
            print('seq_id\tpident\tgenus\tspecies')
        else:
            out_file_fh = open(out_file, 'w+')
            out_file_fh.write('seq_id\tpident\tgenus\tspecies\n')

        # make a dict called "output" with key = seqid and value = a list of the info we want 
        output = {}
        for row in blast_result:
            output[row['sseqid']] = [row['sseqid'], row['pident'], \
                genus.get(row['sseqid'], 'NA'), species.get(row['sseqid'], 'NA')]

        # iterate over the dict "output" and print to screen or file 
        for key in output:
            if not genus.get(key):
                print('Cannot find seq "' + key + '" in lookup', file=sys.stderr)
            elif not out_file:
                print('\t'.join(output[key]))
            elif out_file and genus.get(key) is not None:
                out_file_fh.write('\t'.join(output[key]))
                out_file_fh.write('\n')
        

# --------------------------------------------------
if __name__ == '__main__':
    main()
