# standard xo

import numpy as np

board = np.zeros(9)

for i in range(4):
    move = int(input("Enter your move (0-8): "))
    board[move] = [1, -1][i % 2]
    print(board)

new_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

