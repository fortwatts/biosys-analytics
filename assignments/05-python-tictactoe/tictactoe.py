#!/usr/bin/env python3
"""
Author : George S. Watts <gwatts@email.arizona.edu>
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
        '-s',
        '--state',
        help='the state of the board (type str, default "........." [9 dots])',
        metavar='str',
        type=str,
        default='.........')

    parser.add_argument(
        '-p',
        '--player',
        help='The player to modify the state (type str, valid "X" or "O", no default)',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-c',
        '--cell',
        help='the cell to alter (type int, valid 1-9, default None)',
        metavar='int',
        type=int,
        default=None)

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
def grid(state):

    print('-------------')
    for index, index_state in enumerate(state, start=1):
        if re.match(r'[XO]', index_state):
            print('| {} '.format(index_state), end='')
        else:
            print('| {} '.format(index), end='')
        if (index) % 3 == 0:
            print('|\n-------------')

def main():
    args = get_args()
    state = args.state
    player = args.player
    cell = args.cell

#   check that the state argument contains only -, X, O
    if not re.match(r'^[XO.]{9}$', state):# and player not None and cell not None:
        print('Invalid state "{}", must be 9 characters of only ., X, O'.format(state))
        sys.exit(1)

#   check that the player argument is X or O
    if player and not re.match(r'[XO]', player):
        print('Invalid player "{}", must be X or O'.format(player))
        sys.exit(1)

#   check that cell is between 1 and 9
    if cell == 0 or (cell is not None and (1 < cell > 9)):
        print('Invalid cell "{}", must be 1-9'.format(cell))
        sys.exit(1)

#   check that we have a player and a cell argument
    if any([player, cell]) and not all([player, cell]):
        print('Must provide both --player and --cell')
        sys.exit(1)

    if all([player,cell]):
        cells = []
        for i, char in enumerate(state, start=1):
            cells.append(str(i) if char == '.' else char)
        if cells[cell-1] not in 'XO':
            cells[cell-1] = player
        else:
            die('Cell {} already taken'.format(cell))
        state = cells

    winning_states = [0,1,2], [3,4,5], [6,7,8], [1,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    print('winning_states is: {}'.format(winning_states))
    print('state is: {}'.format(state))
    print('player is: {}'.format(player))
    if all([state[element] == player for element in winning_states]):
        print('winner is: {}'.format(player))
    
#    grid(state)

# --------------------------------------------------
if __name__ == '__main__':
    main()

