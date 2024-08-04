from typing import List, Optional

Matrix = List[List[int]]


def solve(game: Matrix) -> Matrix:
    empty = find_empty(game)
    if not empty:
        return game

    row, col = empty
    for num in range(1, 10):
        if is_possible(game, row, col, num):
            game[row][col] = num
            if solve(game):
                return game
            game[row][col] = 0

    return None


def find_empty(game: Matrix) -> Optional[tuple[int, int]]:
    for i in range(9):
        for j in range(9):
            if game[i][j] == 0:
                return (i, j)
    return None


def is_possible(game: Matrix, row: int, col: int, num: int) -> bool:
    for i in range(0, 9):
        if game[row][i] == num or game[i][col] == num:
            return False

    x0 = (row//3)*3
    y0 = (col//3)*3

    for i in range(x0, x0+3):
        for j in range(y0, y0+3):
            if game[i][j] == num:
                return False

    return True
