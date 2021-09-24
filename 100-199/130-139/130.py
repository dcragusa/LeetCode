"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
Input: board = [              Output: [
    ["X", "X", "X", "X"],         ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],         ["X", "X", "X", "X"],
    ["X", "X", "O", "X"],         ["X", "X", "X", "X"],
    ["X", "O", "X", "X"]          ["X", "O", "X", "X"]
]                             ]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are
not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped
to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example 2:
Input: board = [["X"]],  Output: [["X"]]
"""

"""
The trick to this is realising that surrounded regions are any Os that are not reachable by other Os following taxicab 
geometry from the edges (as, if a group reaches the edge, it is not surrounded). So our first step is to set up a list
and set of any Os lying on the edges of the board. We then iterate over this list, adding any Os we find via taxicab
geometry until no more Os can be found. We maintain a list and set of the same coordinates, as the set allows for O(1)
lookup but not iteration, and the list allows for iteration but has costly lookups. Finally, we iterate over the board
and convert any Os that are not in the above set to Xs, as we know these must be surrounded.
"""


from itertools import product, chain


def solve(board):
    num_rows, num_cols = len(board), len(board[0])

    o_edges = [
        (row_idx, col_idx) for row_idx, col_idx in
        chain(product([0, num_rows-1], range(num_cols)), product(range(num_rows), [0, num_cols-1]))
        if board[row_idx][col_idx] == 'O'
    ]
    o_edge_set = set(o_edges)

    for row_idx, col_idx in o_edges:
        directions = ((row_idx-1, col_idx), (row_idx+1, col_idx), (row_idx, col_idx-1), (row_idx, col_idx+1))
        for direction_x, direction_y in directions:
            if direction_x < 1 or direction_x > num_rows - 2 or direction_y < 1 or direction_y > num_cols - 2:
                continue
            if (direction_x, direction_y) in o_edge_set:
                continue
            if board[direction_x][direction_y] == 'O':
                o_edges.append((direction_x, direction_y))
                o_edge_set.add((direction_x, direction_y))

    for row_idx, row in enumerate(board):
        for col_idx, val in enumerate(row):
            if val == 'O' and (row_idx, col_idx) not in o_edge_set:
                board[row_idx][col_idx] = 'X'

    return board


assert solve([
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]) == [
    ["X", "X", "X", "X"],
    ["X", "X", "X", "X"],
    ["X", "X", "X", "X"],
    ["X", "O", "X", "X"]
]
assert solve([['X']]) == [['X']]
assert solve([
    ["O", "X", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "X", "O", "O", "O", "O", "X"],
    ["O", "X", "O", "X", "O", "O", "O", "O", "X"],
    ["O", "O", "O", "O", "X", "O", "O", "O", "O"],
    ["X", "O", "O", "O", "O", "O", "O", "O", "X"],
    ["X", "X", "O", "O", "X", "O", "X", "O", "X"],
    ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "X", "X", "O", "O"]
]) == [
    ["O", "X", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "X", "O", "O", "O", "O", "X"],
    ["O", "X", "O", "X", "O", "O", "O", "O", "X"],
    ["O", "O", "O", "O", "X", "O", "O", "O", "O"],
    ["X", "O", "O", "O", "O", "O", "O", "O", "X"],
    ["X", "X", "O", "O", "X", "O", "X", "O", "X"],
    ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "X", "X", "O", "O"]
]
