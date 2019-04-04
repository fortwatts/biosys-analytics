#!/usr/bin/env python3
"""
Author : gwatts
Date   : 2019-03-31
Purpose: parses various date formats to a standard yyyy-mm-dd
"""

import os
import sys
import re

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} DATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    date = args[0]
# !2012-03-09T08:59
# !2012-03-09T08:59:03
# !2017-06-16Z
# !2015-01
# !2015-01/2015-02
# !2015-01-03/2015-02-14
# !20100910
# !12/06
# !2/14
# !2/14-12/15
# !2017-06-16Z
# !Dec-2015
# Dec, 2015
# !March-2017
# April, 2017
    date_re1 = re.compile(
                        '(?P<year>\d{4})' # capture year (group 1)
                        '[/-]' # separator
                        '(?P<month>\d{1,2})' # capture month (group 2)
                        '([-](?P<day>\d{1,2}))?' # capture day with sep and day optional (group 3)
                        )

    date_re2 = re.compile( #20100910
                        '(?P<year>\d{4})' # capture year (group 1)
                        '[/-]?' # separator
                        '(?P<month>\d{2})' # capture month (group 2)
                        '[/-]?'
                        '(?P<day>\d{2})'
                        )

    date_re3 = re.compile( # 12/06 2/14 2/14-12/15
                        '(?P<month>\d{1,2})' # capture year (group 1)
                        '[/]' # separator
                        '(?P<year>\d{2})' # capture month (group 2)
                        '([/](?P<day>\d{1,2}))?' # capture day with sep and day optional (group 3)
                        )

    date_re4 = re.compile( # Dec-2015 March-2017
                        '(?P<month>\w+)' # capture year (group 1)
                        '[,-]' # separator
                        '(?P<year>\d{4})' # capture month (group 2)
                        '([/-](?P<day>\d{1,2}))?' # capture day with sep and day optional (group 3)
                        )

    date_re5 = re.compile(
                        '(?P<month>\w+)' # capture year (group 1)
                        ', ' # separator
                        '(?P<year>\d{4})' # capture month (group 2)
                        '([/-](?P<day>\d{1,2}))?' # capture day with sep and day optional (group 3)
                        )
    match = date_re1.match(date) or date_re2.match(date) or date_re3.match(date) or date_re4.match(date) or date_re5.match(date)
    if match:
        year = match.group('year')
        if len(year) == 2:
            year = '20' + match.group('year')
        month = (match.group('month'))
        short_months = ('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec').split()
        short_mon2num = dict(map(reversed, enumerate(short_months,1)))
        long_months = ('January February March April May June July August September October November December').split()
        long_mon2num = dict(map(reversed, enumerate(long_months,1)))
        if re.match('[a-zA-Z]', month):
            if str(short_mon2num.get(month)) != 'None':
                month = str(short_mon2num.get(month))
            elif str(long_mon2num.get(month)) != 'None':
                month = str(long_mon2num.get(month))
            else:
                pass
        day = match.group('day') or '01'
    # print('match is: {}'.format(match))
    # print('year is: {}'.format(year))
    # print('month is: {}'.format(month))
    # print('day is: {}'.format(match.group('day')))
        print('{:4d}-{:02d}-{:02d}'.format(
            int(year),
            int(month),
            int(day)))
    else:
        print('No match')

# --------------------------------------------------
main()
