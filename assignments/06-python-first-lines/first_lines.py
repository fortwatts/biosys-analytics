#!/usr/bin/env python3
"""
Author : George S. Watts
Date   : 2019-02-27
Purpose: Get first line of every file in input directory with numbered output
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='first lines',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'dir', nargs='+', metavar='in_directory', help='Input directory')

    parser.add_argument(
        '-w',
        '--width',
        help='width of output line',
        metavar='int',
        type=int,
        default=50)

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
    out_width = args.width

    for mydirectory in in_dir:
        if not os.path.isdir(mydirectory):
            warn('"{}" is not a directory'.format(mydirectory))
            continue
        print('{}'.format(mydirectory))
        dict_of_lines = {}
        for file in os.listdir(mydirectory):
            path = os.path.join(mydirectory, file)
            with open(path) as myfile_fh:
                dict_of_lines[myfile_fh.readline().rstrip()] = file
        for line in sorted(dict_of_lines.keys()):
            dots = '.'*(out_width - len(line) - len(dict_of_lines[line]))
            print(line, dots, dict_of_lines[line])    

# --------------------------------------------------
if __name__ == '__main__':
    main()
