"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return the minimum cuts
needed for a palindrome partitioning of s.

Example 1:
Input: s = "aab",  Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a",  Output: 0

Example 3:
Input: s = "ab",  Output: 1
"""

"""
We try and find all possible palindromes in s by expanding outwards from each letter (for odd palindromes, of form aba)
and each gap between letters (of form abba). We keep a dynamic programming array and at each rightmost edge of found
palindromes, we keep the minimum number of cuts required to reach that letter. Once we work our way through the whole
string s, we will have found the minimum number of cuts at the end of the dp array.
"""


def min_cut(s):

    len_s = len(s)
    dp = list(range(len_s))

    def expand_from_center(start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            cuts = 0 if start == 0 else (dp[start-1] + 1)
            dp[end] = min(dp[end], cuts)
            start -= 1
            end += 1

    for i in range(len_s):
        expand_from_center(i, i)
        expand_from_center(i, i+1)

    return dp[len_s-1]


assert min_cut('abcde') == 4
assert min_cut('aab') == 1
assert min_cut('a') == 0
assert min_cut('ab') == 1
assert min_cut('ababababababababababababcbabababababababababababa') == 0
assert min_cut(
    'fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfb'
    'fjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi'
) == 75
assert min_cut(
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
) == 0
