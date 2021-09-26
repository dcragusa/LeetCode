"""
Given a string s and a list of strings wordDict, return True if s can be segmented into a space-separated sequence
of one or more dictionary words. Note that the same word in the dictionary may be reused multiple times.

Example 1:
Input: s = 'leetcode', wordDict = ['leet', 'code'],  Output: True
Explanation: Return True because 'leetcode' can be segmented as 'leet code'.

Example 2:
Input: s = 'applepenapple', wordDict = ['apple', 'pen'],  Output: True
Explanation: Return true because 'applepenapple' can be segmented as 'apple pen apple'.

Example 3:
Input: s = 'catsandog', wordDict = ['cats', 'dog', 'sand', 'and', 'cat'],  Output: False
"""

"""
Firstly, we convert the wordDict into a frozenset (frozen because we won't need to change it afterwards). If s is in 
our dictionary, then we obviously return True. If not, we split s into left and right parts as we count along. If the 
left part is in the dictionary, we recur to check the right part. We memoize this recursive function.
"""

from functools import cache


def word_break(s, wordDict):
    word_set = frozenset(wordDict)
    len_s = len(s)

    @cache
    def helper(s):
        if s in word_set:
            return True
        for i in range(1, len_s):
            if s[:i] in word_set and helper(s[i:]):
                return True
        return False

    return helper(s)


assert word_break('leetcode', ['leet', 'code']) is True
assert word_break('applepenapple', ['apple', 'pen']) is True
assert word_break('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']) is False
assert word_break('ab', ['a', 'b']) is True
