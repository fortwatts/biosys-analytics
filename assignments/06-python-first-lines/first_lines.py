#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2018-11-16
Purpose: Get fields from a tab/csv file
"""

import argparse
import glob
import os
#from collections import OrderedDict
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='first lines',
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
    args = get_args()
    in_dir = args.dir

    for mydirectory in in_dir:
        print('{}'.format(mydirectory))
        if not os.path.isdir(mydirectory):
            warn('"{}" is not a directory'.format(mydirectory))
            continue
        dict_of_lines = {}
        for file in os.listdir(mydirectory):
            path = os.path.join(mydirectory, file)
            with open(path) as myfile_fh:
                dict_of_lines[myfile_fh.readline().rstrip()] = file
        for line in sorted(dict_of_lines.keys()):
            print('{:.<40} {}'.format(line, dict_of_lines[line]))    

# --------------------------------------------------
if __name__ == '__main__':
    main()
