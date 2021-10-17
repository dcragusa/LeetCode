"""
Given an m x n board of characters and a list of strings words, return all words on the board. Each word must be
constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically
neighbouring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
], words = ['oath', 'pea', 'eat', 'rain'],  Output: ['eat', 'oath']

Example 2:
Input: board = [['a', 'b'], ['c', 'd']], words = ['abcb'],  Output: []
"""

"""
This is similar to problem 79. We first go through the list of given words to set up a set of all letters, starting
letters, and letter counters per word. We then go through the board. We can skip letters not in the previously found
set of letters present in the words. We add all remaining letters to an index map and board counter. We also add the 
coords of starting letters to a set. 
The next step is to compare word counters with the board counter, and remove any words that cannot be found in the
board because there are not enough letters. Finally, we go through the remaining words, and perform a DFS on the board,
keeping track of previously visited coords. We add found words to the list to be returned, and break the loop early
when a match is found to avoid double-counting results.
"""


from collections import Counter


def find_words(board, words):
    word_letters = set()
    starting_letters = set()
    word_counters = {}
    for word in words:
        word_counters[word] = Counter()
        for idx, char in enumerate(word):
            if idx == 0:
                starting_letters.add(char)
            word_letters.add(char)
            word_counters[word][char] += 1

    index_map = {}
    start_coords = set()
    board_counter = Counter()
    for row_idx, row in enumerate(board):
        for col_idx, val in enumerate(row):
            if val not in word_letters:
                continue
            coords = row_idx, col_idx
            if val in starting_letters:
                start_coords.add(coords)
            index_map[coords] = val
            board_counter[val] += 1

    word_set = set(words)
    for word in word_counters:
        if any(word_counters[word][char] > board_counter[char] for char in word):
            word_set.remove(word)

    found_words = []

    def dfs(node, word, word_idx, path):
        if word_idx == len(word):
            found_words.append(word)
            return True
        row, col = node
        for coords in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
            if (
                index_map.get(coords) == word[word_idx]
                and coords not in path
                and dfs(coords, word, word_idx + 1, path | {coords})
            ):
                return True

    for word in word_set:
        for coords in start_coords:
            if index_map[coords] == word[0] and dfs(coords, word, 1, {coords}):
                break

    return found_words


board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]
assert sorted(find_words(board, ['oath', 'pea', 'eat', 'rain'])) == ['eat', 'oath']
assert find_words([['a', 'b'], ['c', 'd']], ['abcb']) == []
assert sorted(find_words(board, ['oa', 'oaa'])) == ['oa', 'oaa']
