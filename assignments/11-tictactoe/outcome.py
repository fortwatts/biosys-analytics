#!/usr/bin/env python3
"""
Author : George S. Watts <gwatts@email.arizona.edu>
Date   : 2019-02-07
Purpose: tictactoe script using commandline flagged arguments
"""

import sys
import os
import re

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} STATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    state = args[0]
#   check that the state argument contains only -, X, O
    if not re.match(r'^[XO.]{9}$', state):# and player not None and cell not None:
        print('State "{}" must be 9 characters of only ., X, O'.format(state))
        sys.exit(1)

    cells = []
    for i, char in enumerate(state, start=1):
        cells.append(str(i) if char == '.' else char)
    # print('cells is: {}'.format(cells))
    
    winning_states = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    # print('winning_states is: {}'.format(winning_states))

    for player in ['X','O']:    
        for element in winning_states:
            if all([cells[cell] == player for cell in element]):
                print('{} has won'.format(player))
                sys.exit()
    print('No winner')
# --------------------------------------------------
if __name__ == '__main__':
    main()

