"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

Note:
The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""

"""
First, as in problem 36, we set up 9 sets each for rows, columns and quadrants. This time we know the given board is 
valid, so we go through the board and add each number to the sets. We add each open cell to a dictionary with a set 
of all 9 possibilities.
Once we have set up our sets and dict, we can implement 'shaving', that is, repeatedly going through the open dict and
checking each open cell to see if there is only one possible number. If so, we update the board and all sets, and 
delete the cell from the open dict. Simple Sudokus can be entirely solved this way. If no cells are solved through an 
entire iteration of the open dict, we must solve the remainder of the board in a different way.
We can do this by backtracking: take the first item of the unsolved dictionary (taking advantage of Python's ordered
dictionaries) and go through the available options depth first. If an option leads to a failure later down the line, we
examine the next option in turn until we have no further unsolved cells.
"""


from copy import deepcopy
from itertools import product
from functools import lru_cache


quadrant_cell_mapping = {
    0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2], 3: [3, 4, 5],
    4: [3, 4, 5], 5: [3, 4, 5], 6: [6, 7, 8], 7: [6, 7, 8], 8: [6, 7, 8]
}


@lru_cache()
def get_row_col_quadrant_cells(cell):
    row_idx, col_idx = cell
    row_cells = {(row_idx, c) for c in range(0, 9)}
    col_cells = {(r, col_idx) for r in range(0, 9)}
    quadrant_cells = set(product(quadrant_cell_mapping[row_idx], quadrant_cell_mapping[col_idx]))
    return row_cells, col_cells, quadrant_cells


def backtrack(board, unsolved_copy):
    if not unsolved_copy:
        return True
    cell, options = next(iter(unsolved_copy.items()))
    if not options:
        return False
    row_idx, col_idx = cell
    for option in options:
        board, unsolved_new_copy = board, deepcopy(unsolved_copy)
        row_cells, col_cells, quadrant_cells = get_row_col_quadrant_cells(cell)
        for cell_copy, options_copy in unsolved_new_copy.items():
            if cell_copy in row_cells or cell_copy in col_cells or cell_copy in quadrant_cells:
                unsolved_new_copy[cell_copy].discard(option)
        del unsolved_new_copy[cell]
        if not all(unsolved_new_copy.values()):
            continue
        board[row_idx][col_idx] = option
        if backtrack(board, unsolved_new_copy):
            return True


def solve_sudoku(board):
    rows, cols, quadrants = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
    unsolved = {}
    for row_idx, row in enumerate(board):
        for col_idx, num in enumerate(row):
            if num == '.':
                unsolved[(row_idx, col_idx)] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
            else:
                rows[row_idx].add(num)
                cols[col_idx].add(num)
                quadrant_idx = (row_idx//3)*3 + col_idx//3
                quadrants[quadrant_idx].add(num)

    while unsolved:
        solved = []
        for cell, options in unsolved.items():
            row_idx, col_idx = cell
            quadrant_idx = (row_idx//3)*3 + col_idx//3
            row, col, quadrant = rows[row_idx], cols[col_idx], quadrants[quadrant_idx]
            options -= (row | col | quadrant)
            if len(options) == 1:
                num = options.pop()
                row.add(num), col.add(num), quadrant.add(num)
                board[row_idx][col_idx] = num
                solved.append(cell)
            else:
                unsolved[cell] = options
        if not solved:
            break
        for cell in solved:
            del unsolved[cell]

    backtrack(board, deepcopy(unsolved))


board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]
solve_sudoku(board)
assert board == [
    ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
    ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
    ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
    ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
    ['3', '4', '5', '2', '8', '6', '1', '7', '9']
]
