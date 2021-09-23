"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
beginWord -> s1 -> s2 -> ... -> endWord such that:

    Every adjacent pair of words differs by a single letter.
    Every si is in wordList. Note that beginWord does not need to be in wordList.

Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences
from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list
of the words [beginWord, s1, s2, ..., endWord].

Example 1:
Input: beginWord = 'hit', endWord = 'cog', wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
Output: [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]
Explanation: There are 2 shortest transformation sequences:
'hit' -> 'hot' -> 'dot' -> 'dog' -> 'cog'
'hit' -> 'hot' -> 'lot' -> 'log' -> 'cog'

Example 2:
Input: beginWord = 'hit', endWord = 'cog', wordList = ['hot','dot','dog','lot','log']
Output: []
Explanation: The endWord 'cog' is not in wordList, therefore there is no valid transformation sequence.
"""

"""
First we set up a dictionary of wildcards so we can easily see what words in the word list are obtainable from 
replacing a particular letter. We then perform a breadth-first search: starting from beginWord, we set up a queue of 
paths. We can see from the wildcard dictionary what words we can obtain from replacing each letter in the given word. 
We add each of these into the path and add that to the queue. After each breadth search of the queue, we can add all
matched words of that level to a set of seen words that we exclude from matching (as these would be guaranteed to 
result in a longer path). Once we find a set of results, we can terminate after that breadth search, as any further 
matches would be longer.
"""

from collections import defaultdict, deque


def find_ladders(beginWord, endWord, wordList):

    wildcards = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            wild = word[:i] + '*' + word[i + 1:]
            wildcards[wild].append(word)

    results = []
    queue = deque([[beginWord]])
    seen = set()

    while queue:
        queue_size = len(queue)
        matched = []

        for _ in range(queue_size):
            path = queue.popleft()
            word = path[-1]
            if word == endWord:
                results.append(path)
                continue
            for i in range(len(word)):
                wild = word[:i] + '*' + word[i + 1:]
                for match in wildcards[wild]:
                    if match not in seen:
                        queue.append(path + [match])
                        matched.append(match)

        for match in matched:
            seen.add(match)
        if results:
            break

    return results


assert find_ladders('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']) == [
    ['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']
]
assert find_ladders('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']) == []
assert find_ladders('qa', 'sq', [
    'si', 'go', 'se', 'cm', 'so', 'ph', 'mt', 'db', 'mb', 'sb', 'kr', 'ln', 'tm', 'le', 'av', 'sm',
    'ar', 'ci', 'ca', 'br', 'ti', 'ba', 'to', 'ra', 'fa', 'yo', 'ow', 'sn', 'ya', 'cr', 'po', 'fe',
    'ho', 'ma', 're', 'or', 'rn', 'au', 'ur', 'rh', 'sr', 'tc', 'lt', 'lo', 'as', 'fr', 'nb', 'yb',
    'if', 'pb', 'ge', 'th', 'pm', 'rb', 'sh', 'co', 'ga', 'li', 'ha', 'hz', 'no', 'bi', 'di', 'hi',
    'qa', 'pi', 'os', 'uh', 'wm', 'an', 'me', 'mo', 'na', 'la', 'st', 'er', 'sc', 'ne', 'mn', 'mi',
    'am', 'ex', 'pt', 'io', 'be', 'fm', 'ta', 'tb', 'ni', 'mr', 'pa', 'he', 'lr', 'sq', 'ye'
]) == [
    ['qa', 'ca', 'cm', 'sm', 'sq'], ['qa', 'ca', 'ci', 'si', 'sq'], ['qa', 'ca', 'cr', 'sr', 'sq'],
    ['qa', 'ca', 'co', 'so', 'sq'], ['qa', 'ba', 'br', 'sr', 'sq'], ['qa', 'ba', 'bi', 'si', 'sq'],
    ['qa', 'ba', 'be', 'se', 'sq'], ['qa', 'ra', 're', 'se', 'sq'], ['qa', 'ra', 'rn', 'sn', 'sq'],
    ['qa', 'ra', 'rh', 'sh', 'sq'], ['qa', 'ra', 'rb', 'sb', 'sq'], ['qa', 'fa', 'fe', 'se', 'sq'],
    ['qa', 'fa', 'fr', 'sr', 'sq'], ['qa', 'fa', 'fm', 'sm', 'sq'], ['qa', 'ya', 'yo', 'so', 'sq'],
    ['qa', 'ya', 'yb', 'sb', 'sq'], ['qa', 'ya', 'ye', 'se', 'sq'], ['qa', 'ma', 'mt', 'st', 'sq'],
    ['qa', 'ma', 'mb', 'sb', 'sq'], ['qa', 'ma', 'me', 'se', 'sq'], ['qa', 'ma', 'mo', 'so', 'sq'],
    ['qa', 'ma', 'mn', 'sn', 'sq'], ['qa', 'ma', 'mi', 'si', 'sq'], ['qa', 'ma', 'mr', 'sr', 'sq'],
    ['qa', 'ga', 'go', 'so', 'sq'], ['qa', 'ga', 'ge', 'se', 'sq'], ['qa', 'ha', 'ho', 'so', 'sq'],
    ['qa', 'ha', 'hi', 'si', 'sq'], ['qa', 'ha', 'he', 'se', 'sq'], ['qa', 'na', 'nb', 'sb', 'sq'],
    ['qa', 'na', 'no', 'so', 'sq'], ['qa', 'na', 'ne', 'se', 'sq'], ['qa', 'na', 'ni', 'si', 'sq'],
    ['qa', 'la', 'ln', 'sn', 'sq'], ['qa', 'la', 'le', 'se', 'sq'], ['qa', 'la', 'lt', 'st', 'sq'],
    ['qa', 'la', 'lo', 'so', 'sq'], ['qa', 'la', 'li', 'si', 'sq'], ['qa', 'la', 'lr', 'sr', 'sq'],
    ['qa', 'ta', 'tm', 'sm', 'sq'], ['qa', 'ta', 'ti', 'si', 'sq'], ['qa', 'ta', 'to', 'so', 'sq'],
    ['qa', 'ta', 'tc', 'sc', 'sq'], ['qa', 'ta', 'th', 'sh', 'sq'], ['qa', 'ta', 'tb', 'sb', 'sq'],
    ['qa', 'pa', 'ph', 'sh', 'sq'], ['qa', 'pa', 'po', 'so', 'sq'], ['qa', 'pa', 'pb', 'sb', 'sq'],
    ['qa', 'pa', 'pm', 'sm', 'sq'], ['qa', 'pa', 'pi', 'si', 'sq'], ['qa', 'pa', 'pt', 'st', 'sq']
]

