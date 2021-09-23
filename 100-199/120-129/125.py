"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:
Input: s = "A man, a plan, a canal: Panama",  Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car",  Output: false
Explanation: "raceacar" is not a palindrome.
"""

"""
Pretty easy: we lowercase the string with casefold, then regex remove all non-alphanumeric characters. Then we just
check whether the string is equal to its reverse. 
"""

import re


def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s.casefold())
    return s == s[::-1]


assert is_palindrome("A man, a plan, a canal: Panama") is True
assert is_palindrome("race a car") is False
assert is_palindrome("ab_a") is True
