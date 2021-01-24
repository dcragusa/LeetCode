"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' indicate a queen and an empty space respectively.

Example:
Input: 4
Output: [['. Q . .',  // Solution 1
          '. . . Q',
          'Q . . .',
          '. . Q .'],
         ['. . Q .',  // Solution 2
          'Q . . .',
          '. . . Q',
          '. Q . .']]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""

"""
If n is 1 the solution is trivial. For 1 <= n <= 3 there are no solutions. For n >= 4, we proceed by creating an n x n
board filled with some other character representing unassigned spaces, here '-'. We then use backtracking: we fix one
queen at a time in any '-' position. We then set the rest of the row, and the appropriate squares in the rows below, to
'.'. We then recur downwards, attempting to set a queen in the next row. If we can set a queen in the final row, we
have found a solution. If there are no '-' squares in a row, the current arrangement does not have a valid solution so 
we backtrack.
"""


def solve_n_queens(n):

    if n == 1:
        return [['Q']]
    elif n < 4:
        return []

    def place_queen_on_row(row_idx, board):
        results = []
        for col_idx, col in enumerate(board[row_idx]):
            if col != '-':
                continue
            board_c = board.copy()
            board_c[row_idx] = f"{'.'*col_idx}Q{'.'*(n-1-col_idx)}"
            if row_idx == n - 1:
                return [board_c]
            for below_step in range(1, n-row_idx):
                new_below_row = ''
                for below_col_idx, char in enumerate(board_c[row_idx+below_step]):
                    new_below_row += '.' if (
                            char == '.' or below_col_idx in {col_idx-below_step, col_idx, col_idx+below_step}
                    ) else '-'
                board_c[row_idx+below_step] = new_below_row
            if res := place_queen_on_row(row_idx+1, board_c):
                results.extend(res)
        return results

    board = ['-'*n for _ in range(n)]
    return place_queen_on_row(0, board)


assert solve_n_queens(4) == [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]
assert len(solve_n_queens(8)) == 92
