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
        description='Segregate FASTA sequences by GC content',
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
        default='centroids.csv')

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

    print('blast_hits is: {} and out_file is: {} and annotations file is: {}'.format(blast_hits, out_file, annotation_file))

    genus_species = {}
    with open(annotation_file, 'rU') as annotation_file_fh:
        annotations = csv.reader(annotation_file_fh, delimiter=',')
        for row in annotations:
            genus_species[row[0]] = row[6]+row[7]

    with open(blast_hits, 'rU') as blast_hits_fh:
        blast_result = csv.reader(blast_hits_fh, delimiter='\t')
        for row in blast_result:
            print('read id: {} has genus species: {}'.format(row[1],genus_species.get([row[1]], 'No genus_species')))

    print('I made a change here and its pretty good')

# with open('data.csv','r') as f:
#     next(f) # skip headings
#     reader=csv.reader(f,delimiter='\t')

    # os.makedirs(out_dir, mode=511, exist_ok=True)
    # total_reads = 0 
    # for file in in_dir:
    #     if not os.path.isfile(file):
    #         warn('"{}" is not a file'.format(file))
    #         continue

    #     base, ext = os.path.splitext(os.path.basename(file))
    #     out_high_fh   = open((os.path.join(out_dir, base + '_high' + ext)), 'w')
    #     out_low_fh    = open((os.path.join(out_dir, base + '_low' + ext)), 'w')

    #     with open(file, "rU") as file_fh:
    #         for record in SeqIO.parse(file_fh, "fasta"):
    #             total_reads += 1
    #             i = 0
    #             j = 0
    #             for nucleotide in record.seq:
    #                 i += 1
    #                 if nucleotide in 'GC':
    #                     j += 1
    #             if (100*(j/i)) >= percent:
    #                 SeqIO.write(record, out_high_fh, "fasta")
    #             else:
    #                 SeqIO.write(record, out_low_fh, "fasta")
    # print('Done, wrote {} sequences to out dir "{}"'.format(total_reads,out_dir))

# --------------------------------------------------
if __name__ == '__main__':
    main()
