from typing import List

from homework7.hw3 import tic_tac_toe_checker


def easy_board_view(board: List[List]):
    """
    Print board  in comfortable representation

    :param board: Input list
    """
    print()
    for el in board:
        print(el)


def test_x_wins_case():
    """Testing that we get correct answer
    if we have x wins situation"""

    board = [["-", "-", "o"], ["-", "x", "o"], ["x", "x", "x"]]
    easy_board_view(board)

    assert tic_tac_toe_checker(board) == "x wins!"


def test_o_wins_case():
    """Testing that we get correct answer
    if we have o wins situation"""

    board = [["-", "-", "o"], ["-", "x", "o"], ["x", "x", "o"]]
    easy_board_view(board)

    assert tic_tac_toe_checker(board) == "o wins!"


def test_unfinished_game_case():
    """Testing that we get correct answer
    if we have an unfinished game"""

    board = [["-", "-", "o"], ["-", "x", "o"], ["x", "x", "-"]]
    easy_board_view(board)

    assert tic_tac_toe_checker(board) == "unfinished"


def test_draw_game_case():
    """Testing that we get correct answer
    if we have a draw game"""

    board = [["x", "o", "o"], ["o", "x", "x"], ["x", "o", "o"]]
    easy_board_view(board)

    assert tic_tac_toe_checker(board) == "draw"
