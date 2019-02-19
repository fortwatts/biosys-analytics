#!/usr/bin/env python3
"""
Author : gwatts
Date   : 2019-02-14
Purpose: Rock the Casbah
"""

import os
import sys
from collections import Counter

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} DNA'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    dna = args[0]

    print('DNA is "{}"'.format(dna))

    counts = {}


    for char in dna:
       print(char)
       if char not in counts:
           counts[char] = 0
       counts[char] += 1

    print(' '.join([str(counts['A']), str(counts['C']), str(counts['T']), str(counts['G'])]))
    print' '.join(map(str, [counts['A'], counts['C'], counts['T'], counts['G']]))
    print('{} {} {} {}'.format(counts['A'], counts['C'], counts['T'], counts['G']))
    print('A = {}'.format(counts.get('A', 0)))

    print(Counter(dna))


# --------------------------------------------------
main()
