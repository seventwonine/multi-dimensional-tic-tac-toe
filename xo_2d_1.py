# standard xo

import numpy as np

board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

for i in range(9):
    turn = ["X", "O"][i % 2]
    move = int(input("Enter your move 1-9."))
    board[(move-1)//3][(move-1)%3] = turn
    print(board)
    for j in range(3):
        if board[j][0] == board[j][1] == board[j][2] == turn:
            print(f'{turn} wins!')
            break
        elif board[0][j] == board[1][j] == board[2][j] == turn:
            print(f'{turn} wins!')
            break
    if board[0][0] == board[1][1] == board[2][2] == turn:
        print(f'{turn} wins!')
        break
    if board[2][0] == board[1][1] == board[0][2] == turn:
        print(f'{turn} wins!')
        break

