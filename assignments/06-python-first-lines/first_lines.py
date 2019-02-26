#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2018-11-16
Purpose: Get fields from a tab/csv file
"""

import argparse
import glob
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
        'dir', nargs='+', metavar='in_directory', help='Input directory')
    
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
    in_dir = args.dir

    for directory in in_dir:
        print('directory is:'.format(directory))
        if not os.path.isdir(directory):
            warn('"{}" is not a directory'.format(directory))

    for file in os.listdir(in_dir):
        print('file is:'.format(file))
"""     path = os.path.join(dirname, file)
        with open(file) as myfile_fh:
            reader = csv.DictReader(myfile_fh, delimiter='\n') # use , or \t for csv or tab-delimited
            i = 0
            for row in reader:
                if i == 0:
                    print(row,base)
                else:
                    pass
 """
# --------------------------------------------------
if __name__ == '__main__':
    main()
