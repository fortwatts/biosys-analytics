#!/usr/bin/env python3
"""
Author : gwatts
Date   : 2019-02-17
Purpose: translate RNA or DNa sequence to protein
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='STR', help='DNA/RNA sequence')

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codon translations)',
        required=True,
        metavar='FILE',
        type=str,
        default='None')

    parser.add_argument(
        '-o',
        '--outfile',
        help='A file with codon translations',
        metavar='FILE',
        type=str,
        default='out.txt')

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
    codonfile = args.codons
    outfilename = args.outfile
    sequence = args.positional.upper()

    if not os.path.isfile(codonfile):
        print('--codons "{}" is not a file'.format(codonfile))
        sys.exit(1)

    codon_table = {}
    for line in open(codonfile):
        pairs = line.rstrip('\n').split()
        amino_acid = pairs[1]
        codon = pairs[0]
        codon_table[codon] = amino_acid

    outfile = open(outfilename, 'w')
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i + 3]
        if codon in codon_table:
            amino_acid = codon_table[codon]
            outfile.write(amino_acid)
        else:
            outfile.write('-')
    outfile.write('\n')
    print('Output written to "{}"'.format(outfilename))

    
# --------------------------------------------------
if __name__ == '__main__':
    main()
