"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""

from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    Checks for the state of the tic-tac-toe game

    :param board: Current game board view
    :return: State of the game
    """

    board_transposed = [[board[j][i] for j in range(3)] for i in range(3)]
    board_diags = [
        [board[i][i] for i in range(3)],
        [board[i][2 - i] for i in range(3)],
    ]

    for row in board + board_transposed + board_diags:
        if len(set(row)) == 1 and row[0] != "-":
            return f"{row[0]} wins!"

    if "-" not in [el for row in board for el in row]:
        return "draw"

    return "unfinished"
