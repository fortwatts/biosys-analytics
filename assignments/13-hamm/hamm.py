#!/usr/bin/env python3
"""
Author : George S. Watts
Date   : 2019-04-09
Purpose: Rock the Casbah
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
def dist(words):
    k = 0
    for twople in words:
        for i, j in twople:
            if i == j:
                pass# print('letters match')
            else:
                k += 1
                # print('incremented k')
    return(k)
# --------------------------------------------------
def main():

    args = get_args()
    pos_arg = args.positional
    print('args is: "{}"'.format(args))
    print('positional arguments are: "{}"'.format(pos_arg))

    prg = sys.argv[0]
    prg_name, _ = os.path.splitext(os.path.basename(prg))
    logging.basicConfig(
        filename=prg_name + '.log',
        filemode='a',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    f1, f2 = pos_arg
    if not os.path.isfile(f1):
        die('"{}" is not a file'.format(f1))
    if not os.path.isfile(f2):
        die('"{}" is not a file'.format(f2))
    fh_1 = open(f1)
    fh_2 = open(f2)
    words = list(zip(fh_1.read(), fh_2.read()))
    # print(words)
    dist(words)
    sum(map(dist, words))

# --------------------------------------------------
if __name__ == '__main__':
    main()
