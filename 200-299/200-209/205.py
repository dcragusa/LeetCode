"""
Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in
s can be replaced to get t. All occurrences of a character must be replaced with another character while preserving
the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = 'egg', t = 'add', Output: True

Example 2:
Input: s = 'foo', t = 'bar', Output: False

Example 3:
Input: s = 'paper', t = 'title', Output: True
"""

"""
First we check that the two strings are of equal length: if they aren't, it is impossible for they to be isomorphic.
We then build up two maps: one of s to t, and vice versa. We iterate across both s and t. If the characters are not
found in both maps, then we add them. If they are in one map but not the other, or the characters do not match, then
the strings are not isomorphic.
"""


def is_isomorphic(s, t):

    if len(s) != len(t):
        return False

    s_to_t_map = {}
    t_to_s_map = {}

    for s_char, t_char in zip(s, t):
        if s_char not in s_to_t_map and t_char not in t_to_s_map:
            s_to_t_map[s_char] = t_char
            t_to_s_map[t_char] = s_char
        elif (
            (s_char in s_to_t_map and t_char not in t_to_s_map) or
            (t_char in t_to_s_map and s_char not in s_to_t_map) or
            (s_to_t_map[s_char] != t_char or t_to_s_map[t_char] != s_char)
        ):
            return False
    return True


assert is_isomorphic('egg', 'add') is True
assert is_isomorphic('foo', 'bar') is False
assert is_isomorphic('paper', 'title') is True
assert is_isomorphic('badc', 'baba') is False
