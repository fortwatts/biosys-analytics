#!/usr/bin/env python3
"""
Author : George S. Watts
Date   : 2019-04-09
Purpose: Hamming distance calculator for text files
"""

import argparse
import sys
import logging
import os


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', nargs=2, metavar='FILE', help='File inputs')

    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true')

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
# dist is a function returning an integer and words is a zip of the files split on words.
def dist(s1, s2):
    distance = abs(len(s1) - len(s2))
    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            distance += 1
    logging.debug('s1 = {}, s2 = {}, d = {}'.format(s1, s2, distance))
    return distance
# --------------------------------------------------
def main():
    args = get_args()
    pos_arg = args.positional
    f1, f2 = pos_arg

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)
    logging.debug('args is: "{}"'.format(args))
    # logging.debug('positional arguments are: "{}"'.format(pos_arg))
    # logging.debug('file1 = {} and file 2 = {}'.format(f1, f2))

    if not os.path.isfile(f1):
        die('"{}" is not a file'.format(f1))
    if not os.path.isfile(f2):
        die('"{}" is not a file'.format(f2))
    words_1 = open(f1).read().split()
    words_2 = open(f2).read().split()
    # total_dist = sum(map(dist, zip(words_1, words_2)))
    total_dist = 0
    for s1, s2 in zip(words_1, words_2):
        total_dist += dist(s1, s2)
    print(total_dist)

# --------------------------------------------------
if __name__ == '__main__':
    main()