#!/usr/bin/env python3
"""
Author : George S. Watts <fortwatts@gmail.com>
Date   : 2019-03-08
Purpose: annotate BLAST poutput with genus and species from annotation file 
"""

import csv
import argparse
import os
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

    for file in [blast_hits, annotation_file]:
        if not os.path.isfile(file):
<<<<<<< HEAD
            die('"{}" is not a file'.format(blast_hits))
=======
            die('"{}" is not a file'.format(file))
>>>>>>> 31d63f0e3bea272fe40ee82f6f57f96b63cd4ee4

    # if not os.path.isfile(blast_hits):
    #     die('"{}" is not a file'.format(blast_hits))
    # if not os.path.isfile(annotation_file):
    #     die('"{}" is not a file'.format(annotation_file))

    #create 2 dicts of key = sequence_id and value = genus or species
    species = {}
    genus = {}
    with open(annotation_file, 'r') as annotation_file_fh:
        annotations = csv.DictReader(annotation_file_fh, delimiter=',')
        for row in annotations:
            genus[row['centroid']] = row['genus']
            species[row['centroid']] = row['species']

    with open(blast_hits, 'r') as blast_hits_fh:
        blast_result = csv.DictReader(blast_hits_fh, fieldnames=['qseqid', 'sseqid', 'pident', \
            'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore'], delimiter='\t')
        # set up output headers
#       out_fh = open(out_file, 'wt') if out_file else sys.stdout
        if not out_file:
            print('seq_id\tpident\tgenus\tspecies')
        else:
            out_file_fh = open(out_file, 'w+')
            out_file_fh.write('seq_id\tpident\tgenus\tspecies\n')
        # make a dict called "output" with key = seqid and value = a list of the info we want 
        output = {}
        for row in blast_result:
            output[row['sseqid']] = [row['sseqid'], row['pident'], \
                (genus.get(row['sseqid']) or 'NA'), (species.get(row['sseqid']) or 'NA')]
        # iterate over the dict and print to screen or file 
        for key in output:
            if genus.get(key) == None:
                print('Cannot find seq "' + key + '" in lookup', file=sys.stderr)
            elif not out_file:
                print('\t'.join(output[key]))
            elif genus.get(key) or genus.get(key) == '':
                out_file_fh.write('\t'.join(output[key]))
                out_file_fh.write('\n')

# --------------------------------------------------
if __name__ == '__main__':
    main()
