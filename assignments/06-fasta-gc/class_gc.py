#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2018-11-16
Purpose: Get fields from a tab/csv file
"""

import argparse
import os
from Bio import SeqIO
from collections import Counter
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Segregate FASTA sequences by GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fasta', nargs='+', metavar='FILE', help='Input FASTA file(s)')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='out')

    parser.add_argument(
        '-p',
        '--pct_gc',
        help='Dividing line for percent GC',
        metavar='int',
        type=int,
        default='50')

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
    fasta = args.fasta
    out_dir = args.outdir
    percent = (args.pct_gc)

    if (1 > percent) or (percent > 100):
        die('--pct_gc "{}" must be between 0 and 100'.format(percent))

    os.makedirs(out_dir, mode=511, exist_ok=True)
    total_reads = 0 
    for file in fasta:
        if not os.path.isfile(file):
            warn('"{}" is not a file'.format(file))
            continue

        base, ext = os.path.splitext(os.path.basename(file))
        out_high_fh   = open((os.path.join(out_dir, base + '_high' + ext)), 'w')
        out_low_fh    = open((os.path.join(out_dir, base + '_low' + ext)), 'w')

        with open(file, "rU") as file_fh:
            for record in SeqIO.parse(file_fh, "fasta"):
                nucls = Counter(record.seq)
                seq_len = len(record.seq)
                gc = nucls.get('G', 0) + nucls.get('C', 0)
                print('per is {}'.format(100*(gc/seq_len)))
                if (100*(gc/seq_len)) >= percent:
                    SeqIO.write(record, out_high_fh, "fasta")
                else:
                    SeqIO.write(record, out_low_fh, "fasta")
    print('Done, wrote {} sequences to out dir "{}"'.format(total_reads,out_dir))


# --------------------------------------------------
if __name__ == '__main__':
    main()
