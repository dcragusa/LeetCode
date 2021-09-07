"""
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of
sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:
board = [['A', 'B', 'C', 'E'],
         ['S', 'F', 'C', 'S'],
         ['A', 'D', 'E', 'E']]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

Constraints:
board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""

"""
We make an initial pass over the board and set up a counter of the letters present in word, an index map for later 
O(1) access, and a list of coords of the first letter in the word. We then check if there are enough letters in the 
board to fill word, if not we return False immediately with no searching.
We then perform a depth first search for the rest of the word: for each letter, we check if it contained in the cells 
around the starting coords. If this is the last letter, we have found the entire word and return True upwards. If not,
we add the current cell to the set of visited cells and recur downwards with the appropriate starting cell, visited 
cells, and next letter of the word.
"""


from collections import Counter


def word_exists(board, word):

    word_set = set(word)
    word_counter = Counter(word)
    board_counter = Counter()
    board_idx_map = {}
    starting = []

    for r_idx, row in enumerate(board):
        for c_idx, val in enumerate(row):
            if val in word_set:
                board_counter[val] += 1
                board_idx_map[(r_idx, c_idx)] = val
                if val == word[0]:
                    starting.append((r_idx, c_idx))

    if any(board_counter[letter] < word_counter[letter] for letter in word_set):
        return False

    def dfs(origin, visited, word):
        candidates = []
        row, col = origin
        for r_idx, c_idx in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
            coords = (r_idx, c_idx)
            if not (val := board_idx_map.get(coords)) or coords in visited or val != word[0]:
                continue
            elif len(word) == 1:
                return True
            else:
                candidates.append(coords)
        visited.add(origin)
        for coords in candidates:
            if dfs(coords, visited, word[1:]):
                return True
        visited.remove(origin)
        return False

    return bool(starting) if len(word) == 1 else any(dfs(coords, set(), word[1:]) for coords in starting)


board = [['A', 'B', 'C', 'E'],
         ['S', 'F', 'C', 'S'],
         ['A', 'D', 'E', 'E']]

assert word_exists(board, 'ABCCED') is True
assert word_exists(board, 'SEE') is True
assert word_exists(board, 'ABCB') is False
assert word_exists(board, 'ABCSF') is False
assert word_exists(board, 'ABCESCFSADEE') is True
assert word_exists(board, 'ABCESCFSAED') is False
assert word_exists(board, 'AF') is False

assert word_exists([['a']], 'a') is True

assert word_exists([['A', 'B', 'C', 'E'],
                    ['S', 'F', 'E', 'S'],
                    ['A', 'D', 'E', 'E']], 'ABCESEEEFS') is True
