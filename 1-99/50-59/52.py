"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:
Input: 4, Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[[".Q..",  // Solution 1
 "...Q",
 "Q...",
 "..Q."],
 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]]
"""

"""
Same procedure as problem 51 except we propagate the number of results upwards, and not the final state of the board.
"""


def solve_n_queens(n):

    if n == 1:
        return 1
    elif n < 4:
        return 0

    def place_queen_on_row(row_idx, board):
        results = 0
        for col_idx, col in enumerate(board[row_idx]):
            if col != '-':
                continue
            board_c = board.copy()
            board_c[row_idx] = f"{'.'*col_idx}Q{'.'*(n-1-col_idx)}"
            if row_idx == n - 1:
                return 1
            for below_step in range(1, n-row_idx):
                new_below_row = ''
                for below_col_idx, char in enumerate(board_c[row_idx+below_step]):
                    new_below_row += '.' if (
                        char == '.' or below_col_idx in {col_idx-below_step, col_idx, col_idx+below_step}
                    ) else '-'
                board_c[row_idx+below_step] = new_below_row
            if res := place_queen_on_row(row_idx+1, board_c):
                results += res
        return results

    board = ['-'*n for _ in range(n)]
    return place_queen_on_row(0, board)


assert solve_n_queens(4) == 2
assert solve_n_queens(8) == 92
