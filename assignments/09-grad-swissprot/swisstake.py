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
    skips = set([skip.upper() for skip in args.skip])
    # print('skips is: {}'.format(skips))
    keyword = args.keyword

    if not os.path.isfile(in_file):
        die('"{}" is not a file'.format(in_file))

    try:
        os.remove(out_file)
    except OSError:
        pass

    out_file_fh = open(out_file, 'a')
    with open(in_file, 'r') as in_file_fh:
        print('Processing "{}"'.format(in_file))
        records = SeqIO.parse(in_file_fh, 'swiss')
        my_records = []
        i = 0
        k = 0
        j = 0
        for record in records:
            j += 1
            info = record.annotations
            if 'keywords' in info:
                upper_keywords = [x.upper() for x in info['keywords']] 
                if keyword.upper() in upper_keywords:
                    if 'taxonomy' in info:
                        upper_taxa = set([x.upper() for x in info['taxonomy']])
                        if len(skips.intersection(upper_taxa)) == 0:
                            # print('skip words are not in taxa')
                            i += 1
                            j -= 1
                            SeqIO.write(record, out_file_fh, 'fasta')                                
                        else:
                            pass
                            # print('***a SKIP word {} IS in upper_taxa {}'.format(skips, upper_taxa))
                            # print('skipped = {}'.format(k))
    print('Done, skipped {} and took {}. See output in "{}".'.format(j, i, out_file))

# --------------------------------------------------
if __name__ == '__main__':
    main()
