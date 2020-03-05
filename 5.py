"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
"""

"""
We look at all possible centers for palindromes to occur, and expand outwards from those centers.
"""


def find_longest_palindromic_substring(s):
    i, j = 0, 1
    len_s = len(s)
    longest_palindrome = ''
    if len_s < 2:
        return s

    while j < len_s:
        temp_i, temp_j = i, j
        while temp_i >= 0 and temp_j <= len_s - 1 and s[temp_i] == s[temp_j]:
            if temp_j + 1 - temp_i > len(longest_palindrome):
                longest_palindrome = s[temp_i:temp_j+1]
            temp_i -= 1
            temp_j += 1

        if i != j:
            i += 1
        else:
            j += 1

    return longest_palindrome


assert find_longest_palindromic_substring('babad') == 'bab'
assert find_longest_palindromic_substring('cbbd') == 'bb'
