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
    #print('blast_hits is: {} and out_file is: {} and annotations file is: {}'.format(blast_hits, out_file, annotation_file))

    genus_species = {}
    with open(annotation_file, 'rU') as annotation_file_fh:
        annotations = csv.reader(annotation_file_fh, delimiter=',')
        for row in annotations:
            genus_species[row[0]] = row[6] + ' ' + row[7]

    with open(blast_hits, 'rU') as blast_hits_fh:
        blast_result = csv.reader(blast_hits_fh, delimiter='\t')

        if out_file == '':
            print('seq_id\tpident\tgenus\tspecies')
        else:
            out_file_fh = open(out_file, 'w+')
            out_file_fh.write('seq_id\tpident\tgenus\tspecies\n')
        for row in blast_result:
            read_id = (row[1])
            pident = (row[2])
            the_genus_species = genus_species.get(read_id, 'id_not_found')
            if the_genus_species == 'id_not_found':
                print('Cannot find seq "' + read_id + '" in lookup', file=sys.stderr)
            elif out_file:
                #print('printing: {} to out_file'.format(the_genus_species))
                out_file_fh.write('{} {} {}\n'.format(read_id, pident, the_genus_species))
            else:
                print('{} {} {}'.format(read_id, pident, the_genus_species))

# --------------------------------------------------
if __name__ == '__main__':
    main()
