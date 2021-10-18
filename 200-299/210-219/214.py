"""
You are given a string s. You can convert s to a palindrome by adding characters in front of it. Return the shortest
palindrome you can find by performing this transformation.

Example 1:
Input: s = 'aacecaaa', Output: 'aaacecaaa'

Example 2:
Input: s = 'abcd', Output: 'dcbabcd'
"""

"""
Seeing as we can only add letters to the front, this is equivalent to finding the longest palindrome on the left, then
adding the reversed remainder on the right to the start of the string. We thus count from the right leftwards, finding
the first (largest) palindrome, and add the reversed remainder before returning.
"""


def shortest_palindrome(s):
    if not s:
        return s
    for i in reversed(range(len(s)+1)):
        if s[:i] == s[:i][::-1]:
            break
    return s[i:][::-1] + s


assert shortest_palindrome('aacecaaa') == 'aaacecaaa'
assert shortest_palindrome('abcd') == 'dcbabcd'
