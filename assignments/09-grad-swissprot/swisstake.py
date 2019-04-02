#!/usr/bin/env python3
"""
Author : George S. Watts <fortwatts@gmail.com>
Date   : 2019-03-08
Purpose: select swissprot entries based on keyword with taxa keyword exclusion 
"""

import os
import sys
import argparse
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument(
        'file', metavar='FILE', help='Uniprot file')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default='out.fa')

    parser.add_argument(
        '-s',
        '--skip',
        help='Skip taxa',
        metavar='STR',
        type=str, 
        nargs='+',
        default='')

    parser.add_argument(
        '-k',
        '--keyword',
        help='Take on keyword',
        metavar='STR',
        type=str,
        required=True,
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
    in_file = args.file
    out_file = args.outfile
    skips = (args.skip)
    # print(type(skips))
    keyword = args.keyword

    if not os.path.isfile(in_file):
        die('"{}" is not a file'.format(in_file))

    with open(in_file, 'r') as in_file_fh:
        records = SeqIO.parse(in_file_fh, 'swiss')
        my_records = []
        for record in records:
            info = record.annotations
            # print(info['taxonomy'])
            if 'keywords' in info:
                upper_keywords = [x.upper() for x in info['keywords']] 
                if keyword.upper() in upper_keywords:
                    if 'taxonomy' in info:
                        # print('found one {}\n'.format(info))
                        upper_taxa = ([x.upper() for x in info['taxonomy']])
                        for x in skips:
                            if x.upper() not in upper_taxa:
                                my_records.append(record)
                                print('seqid: {} with seq: {}'.format(record.id, record.seq))
                                out_file_fh = open(out_file, 'a')
                                out_file_fh.write('>{}\n{}\n'.format(record.id, record.seq))                                
                            else:
                                pass# print('skipped {} record because {} in taxonomy {}'.format(record.id, x, info['taxonomy']))
        # SeqIO.convert("my_records", "swiss", "swiss.fasta", "fasta")
        # print(my_records)
# use sets here 

# --------------------------------------------------
if __name__ == '__main__':
    main()
