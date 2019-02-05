#!/usr/bin/env python3
"""
Author : gwatts
Date   : 2019-02-03
Purpose: count vowels in useer provided argument
"""

import os
import sys


# --------------------------------------------------
def main():
    phrase = sys.argv[1:]

    if len(phrase) != 1:
        print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    vowel_count = 0
    for letter in phrase[0]:
        if letter == 'a' or letter == 'A' or letter == 'e' or letter == 'E' or letter == 'i' or letter == 'I' or letter == 'o' or letter == 'O' or letter == 'u' or letter == 'U':
            vowel_count += 1

    if vowel_count == 0 or vowel_count >1:
        print ("There are {} vowels in \"{}.\"".format(vowel_count, phrase[0]))
    elif vowel_count == 1:
        print ("There is {} vowel in \"{}.\"".format(vowel_count, phrase[0]))

# --------------------------------------------------
main()
