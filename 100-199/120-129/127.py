"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
beginWord -> s1 -> s2 -> ... -> endWord such that:

    Every adjacent pair of words differs by a single letter.
    Every si is in wordList. Note that beginWord does not need to be in wordList.

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
"""

"""
Same logic as 126 except we do not have to keep track of the path, but only the length and last word. We also return
the length on the first match instead of progressing through the breadth-first-search.
"""

from collections import defaultdict, deque


def find_ladders(beginWord, endWord, wordList):

    wildcards = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            wild = word[:i] + '*' + word[i + 1:]
            wildcards[wild].append(word)

    results = []
    queue = deque([(1, beginWord)])
    seen = set()

    while queue:
        queue_size = len(queue)
        matched = []

        for _ in range(queue_size):
            length, word = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                wild = word[:i] + '*' + word[i + 1:]
                for match in wildcards[wild]:
                    if match not in seen:
                        queue.append((length + 1, match))
                        matched.append(match)

        for match in matched:
            seen.add(match)
        if results:
            break

    return 0


assert find_ladders('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']) == 5
assert find_ladders('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']) == 0
assert find_ladders('qa', 'sq', [
    'si', 'go', 'se', 'cm', 'so', 'ph', 'mt', 'db', 'mb', 'sb', 'kr', 'ln', 'tm', 'le', 'av', 'sm',
    'ar', 'ci', 'ca', 'br', 'ti', 'ba', 'to', 'ra', 'fa', 'yo', 'ow', 'sn', 'ya', 'cr', 'po', 'fe',
    'ho', 'ma', 're', 'or', 'rn', 'au', 'ur', 'rh', 'sr', 'tc', 'lt', 'lo', 'as', 'fr', 'nb', 'yb',
    'if', 'pb', 'ge', 'th', 'pm', 'rb', 'sh', 'co', 'ga', 'li', 'ha', 'hz', 'no', 'bi', 'di', 'hi',
    'qa', 'pi', 'os', 'uh', 'wm', 'an', 'me', 'mo', 'na', 'la', 'st', 'er', 'sc', 'ne', 'mn', 'mi',
    'am', 'ex', 'pt', 'io', 'be', 'fm', 'ta', 'tb', 'ni', 'mr', 'pa', 'he', 'lr', 'sq', 'ye'
]) == 5

