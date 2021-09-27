"""
Given a string s and a list of strings wordDict, add spaces in s to construct a sentence where each word is a valid
dictionary word. Return all such possible sentences in any order. Note that the same word in the dictionary may be
reused multiple times in the segmentation.

Example 1:
Input: s = 'catsanddog', wordDict = ['cat', 'cats', 'and', 'sand', 'dog'],  Output: ['cats and dog', 'cat sand dog']

Example 2:
Input: s = 'pineapplepenapple', wordDict = ['apple', 'pen', 'applepen', 'pine', 'pineapple']
Output: ['pine apple pen apple', 'pineapple pen apple', 'pine applepen apple']

Example 3:
Input: s = 'catsandog', wordDict = ['cats', 'dog', 'sand', 'and', 'cat'],  Output: []
"""

"""
Same logic as 139 except we pass down the sentence so far to our recursive functions, and do not terminate early when
finding a match (as we must find all possible segmentations).
"""


def word_break(s, wordDict):
    word_set = frozenset(wordDict)
    len_s = len(s)

    def helper(s, sentence):
        results = []
        if s in word_set:
            results.append(f'{sentence} {s}'.strip())
        for i in range(1, len_s):
            if (left := s[:i]) in word_set:
                results.extend(helper(s[i:], f'{sentence} {left}'))
        return results

    return helper(s, '')


assert word_break('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog']) == ['cat sand dog', 'cats and dog']
assert word_break(
    'pineapplepenapple', ['apple', 'pen', 'applepen', 'pine', 'pineapple']
) == ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple']
assert word_break('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']) == []
