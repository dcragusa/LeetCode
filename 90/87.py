"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t

To scramble the string, we may choose any non-leaf node and swap its two children.
For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t

We can say that "rgeat" is a scrambled string of "great".
Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a

We can say that "rgtae" is also scrambled string of "great".
Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:
Input: s1 = "great", s2 = "rgeat",  Output: true

Example 2:
Input: s1 = "abcde", s2 = "caebd",  Output: false
"""

"""
At the basest level, two strings are a scramble if they are equal or reversed. Otherwise, we start splitting up the
strings at the verious possible points. We compare character counts for the 4 possible combinations we would obtain
from splitting the string into two nodes at that point: s1_start-s2_start, s1_start-s2_end, s1_end-s2_start, and 
s1_end-s2_end. If the character counts are equal, there is a possible split and we recur down, checking if each half
is a valid scramble on its own. We keep a cache to avoid recalculating if parts of a string are scrambled.
"""

from collections import Counter
from functools import lru_cache


@lru_cache()
def is_scramble(s1, s2):
    if s1 == s2 or s1 == s2[::-1]:
        return True
    for idx in range(1, len(s1)-1):
        s1_start, s1_end, s2_start, s2_end = s1[:idx], s1[-idx:], s2[:idx], s2[-idx:]
        s1_start_counter, s1_end_counter = Counter(s1_start), Counter(s1_end)
        s2_start_counter, s2_end_counter = Counter(s2_start), Counter(s2_end)
        # first {idx} s1 chars valid anagram to start of s2
        if s1_start_counter == s2_start_counter and is_scramble(s1_start, s2_start) and is_scramble(s1[idx:], s2[idx:]):
            return True
        # first {idx} s1 chars valid anagram to end of s2
        if s1_start_counter == s2_end_counter and is_scramble(s1_start, s2_end) and is_scramble(s1[idx:], s2[:-idx]):
            return True
        # last {idx} s1 chars valid anagram to start of s2
        if s1_end_counter == s2_start_counter and is_scramble(s1_end, s2_start) and is_scramble(s1[:-idx], s2[idx:]):
            return True
        # last {idx} s1 chars valid anagram to end of s2
        if s1_end_counter == s2_end_counter and is_scramble(s1_end, s2_end) and is_scramble(s1[:-idx], s2[:-idx]):
            return True
    return False


assert is_scramble('bca', 'abc') is True
assert is_scramble('abcd', 'badc') is True
assert is_scramble('abcd', 'dacb') is True
assert is_scramble('great', 'rgeat') is True
assert is_scramble('abcde', 'caebd') is False
assert is_scramble('abcdd', 'dbdac') is False
assert is_scramble('hobobyrqd', 'hbyorqdbo') is True
assert is_scramble('abcdefghij', 'efghijcadb') is False
assert is_scramble('vfldiodffghyq', 'vdgyhfqfdliof') is True
assert is_scramble('abbbcbaaccacaacc', 'acaaaccabcabcbcb') is True
