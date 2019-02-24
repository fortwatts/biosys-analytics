#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2018-11-16
Purpose: Get fields from a tab/csv file
"""

import argparse
import glob
import os
import re
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Segregate FASTA sequences by GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file', nargs='+', metavar='FASTA', help='Input FASTA file(s)')

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
        type=str,
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
    file_or_dir = args.file
    directory = args.outdir
    percent = args.pct_gc

    print('file_or_dir is {}'.format(file_or_dir))

    for file in file_or_dir:
        print('I have file: {}'.format(file))

    print('file_or_dir is: {}\nand outdir is: {}\nand percent is {}'.format(file_or_dir,directory,percent))

"""     for file in files:

        if not os.path.isfile(file):
            print('"{}" is not a file'.format(file))
            sys.exit(1)

        with open(file, '\n') as file_fh:
                 delim = default_delim
            if not delim:
                _, ext = os.path.splitext(file)
                if ext == '.csv':
                    delim = ','
                else:
                    delim = '\t'

            reader = csv.DictReader(fh, delimiter=delim)

            print(delim.join(field_names))

            for row in reader:
                flds = list(map(lambda f: row[f], field_names))
                print(delim.join(flds))
 """

# --------------------------------------------------
if __name__ == '__main__':
    main()
