#!/usr/bin/env python3
"""
Author : gwatts
Date   : 2019-03-31
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} DATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    date = args[0]

    date_re = re.compile('(\d{4})' # capture year (group 1)
                        '[/-]' # separator
                        '(\d{1,2})' # capture month (group 2)
                        '[/-]' # separator
                        '(\d{1,2})') # capture day (group 3)

    print('date is "{}"'.format(date))


# --------------------------------------------------
main()
