#!/usr/bin/env python3
"""
Author : gwatts
Date   : 2019-02-05
Purpose: Rock the Casbah
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

    lines = []
# read the lines of the file into a list:
    for line in open(file):
        lines.append(line.rstrip('\n'))
# use enumereate on the list:
    for i, listelement in enumerate(lines):
        print('{:3}: {}'.format((i+1),listelement))
# --------------------------------------------------
main()
