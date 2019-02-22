#!/usr/bin/env python3
"""
Author : gwatts@email.arizona.edu
Date   : 2019-02-07
Purpose: tictactoe script using commandline flagged arguments
"""

import argparse
import sys
import re

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='str', help='the state of the board (type str, default "........." [9 dots])')

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
def main():

    args = get_args()
    state = args.positional

    if state == None:
        print('Usage: outcome.py STATE')

#   check that the state argument contains only -, X, O
    if not re.match(r'^[XO.]{9}$', state):
        print('State "{}" must be 9 characters of only ., X, O'.format(state))
        sys.exit(1)

    for side in 'XO':
        for winning_states in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
            if all([state[element] == side for element in winning_states]):
                print('{} has won'.format(side))
                sys.exit(0)

    print('No winner')
    
#    grid(state)

# --------------------------------------------------
if __name__ == '__main__':
    main()

