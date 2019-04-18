#!/usr/bin/env python3
"""
Author : gwatts
Date   : 2019-04-11
Purpose: find overlaps between sequences as a start to a de Bruijn map
"""

import argparse
import sys
import os
import re
from Bio import SeqIO
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='Fasta file')

    parser.add_argument(
        '-k',
        '--overlap',
        help='k-mer length for determining overlap between sequences',
        metavar='integer',
        type=int,
        required = True,
        default=3)

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
def find_kmers(seq, k):
    kmers = []
    if len(seq) < k:
        print('There are no {}-length substrings in "{}"'.format(k, seq))
    else:
        n = len(seq) - k + 1
        for i in range(0, n):
            kmers.append(seq[i:i+k])
    return(kmers)

def main():
    args = get_args()
    overlap = args.overlap
    seqfile = args.positional
    
    # print('overlap = "{}" \nseqfile = "{}"'.format(overlap, seqfile))
    
    if not os.path.isfile(seqfile):
        print('"{}" is not a file'.format(seqfile))
        sys.exit(1)

    if k < 1:
        print('"{}" is not a file'.format(seqfile))
        sys.exit(1)

    first_kmer = defaultdict(list)
    last_kmer = defaultdict(list)

    for record in SeqIO.parse(seqfile, "fasta"):
        seq = str(record.seq)
        kmers = find_kmers(seq, overlap)
        first_kmer[kmers[0]].append(record.id)
        last_kmer[kmers[-1]].append(record.id) 

    for firstkmer, firstids in first_kmer.items():
        for lastkmer, lastids in last_kmer.items():
            if firstkmer == lastkmer:
                # print('first kmer: ', firstkmer, ' = last kmer: ', lastkmer, ' first_ids: ', firstids, ' last_ids: ', lastids, sep='')
                for f_id in firstids:
                    for l_id in lastids:
                        print(f_id, l_id)
# --------------------------------------------------
if __name__ == '__main__':
    main()
