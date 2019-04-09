#!/usr/bin/env python3
"""
Author : George S. Watts
Date   : 2019-04-08
Purpose: Rock the Casbah
"""

import os
import sys
import re


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 2:
        print('Usage: {} PASSWORD ALT'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    passw = args[0]
    alt = args[1]
    passw_re = re.compile('.?'
                        + re.escape(passw) +
                        '.?')
    # print(passw_re.match(alt))
    if passw == alt or passw.upper() == alt.upper() or passw.capitalize() == alt or passw_re.match(alt):
        print('ok')
    else:
        print('nah')
# --------------------------------------------------
main()
