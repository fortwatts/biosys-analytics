#!/usr/bin/env python3
"""
Author : gwatts
Date   : 2019-02-05
Purpose: pytohn script that mimics cat on command line with numbered line option
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = args[0]
    if not os.path.isfile(file):
        print('{} is not a file'.format(file))
        sys.exit(1)

    for i, line in enumerate(open(file)):
        print('{:3}: {}'.format((i+1),line), end='')
# --------------------------------------------------
main()
