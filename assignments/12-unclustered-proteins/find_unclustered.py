#!/usr/bin/env python3
"""
Author : gwatts
Date   : 2019-04-09
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-c',
        '--cdhit',
        help='Output file from CD-HIT (clustered proteins)',
        metavar='str',
        type=str,
        required=True,
        default='None')

    parser.add_argument(
        '-p',
        '--proteins',
        help='Proteins FASTA',
        metavar='str',
        type=str,
        required=True,
        default='None')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='str',
        type=str,
        default='unclustered.fa')

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
    """Make a jazz noise here"""
    args = get_args()
    cdhit = args.cdhit
    proteins = args.proteins
    outfile = args.outfile
    
    if not os.path.isfile(proteins):
        die('--proteins "{}" is not a file'.format(proteins))
    if not os.path.isfile(cdhit):
        die('--cdhit "{}" is not a file'.format(cdhit))

    cluster_list = set()
    with open(cdhit, 'r') as cdhit_fh:
        for line in cdhit_fh:
            match = re.search(r'>gi\|(\d+)\|', line)
            if match:
                cluster_list.add(match.group(1))

    outfile_fh = open(outfile, 'w')
    uncl_i = 0
    total_j = 0
    for record in SeqIO.parse(proteins, "fasta"):
        id = record.id
        total_j += 1
        clean_id = re.sub('\|.*', '', id)
        if clean_id not in cluster_list:
            uncl_i += 1
            SeqIO.write(record, outfile_fh, 'fasta')
    outfile_fh.close()
    print('Wrote {:,} of {:,} unclustered proteins to "{}"'.format(uncl_i, total_j, outfile))

# --------------------------------------------------
if __name__ == '__main__':
    main()
