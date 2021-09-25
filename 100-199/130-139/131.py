"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible
palindrome partitioning of s. A palindrome string is a string that reads the same backwards and forwards.

Example 1:
Input: s = 'aab',  Output: [['a', 'a', 'b'], ['aa', 'b']]

Example 2:
Input: s = 'a',  Output: [['a']]
"""

"""
We count along the entirety of s, splitting it into left and right parts. If the left part is a palindrome, we recur
down with the right part, passing the current path plus the left part down. If we get to an empty sub_s, it means we 
have exhausted s and therefore found a palindrome, so we append the found path to a list of paths.
"""


def partition(s):

    paths = []

    def helper(sub_s, path):
        if not sub_s:
            paths.append(path)
        for i in range(1, len(sub_s)+1):
            left, right = sub_s[:i], sub_s[i:]
            if left == left[::-1]:
                helper(right, path + [left])

    helper(s, [])
    return paths


assert partition('aaa') == [['a', 'a', 'a'], ['a', 'aa'], ['aa', 'a'], ['aaa']]
assert partition('aab') == [['a', 'a', 'b'], ['aa', 'b']]
assert partition('a') == [['a']]
