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

    if len(args) < 1:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    if len(args) < 2:
        num_lines = 3
    else:
        num_lines = int(args[1])

    if num_lines < 1:
       print('lines ({}) must be a positive number'.format(num_lines))
       sys.exit(1)

    file = args[0]
    if not os.path.isfile(file):
        print('{} is not a file'.format(file))
        sys.exit(1)

    lines = []
    for line in open(file):
        lines.append(line.rstrip('\n'))

    i = 0
    while i < num_lines:
        print('{}'.format(lines[i])) 
        i += 1

# for i, line in enumerate(open(filename):
#    print....
#    i + 1 = num_lines
# --------------------------------------------------
main()
