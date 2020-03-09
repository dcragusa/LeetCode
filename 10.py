"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa", p = "a", Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa", p = "a*", Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab", p = ".*", Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab", p = "c*a*b", Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:
Input:
s = "mississippi", p = "mis*is*p*.", Output: false
"""

"""
We go backwards through the string and pattern. If there is a character match and there is no *, advance through the 
string and pattern by one. If there is a *, examine whether combinations of consuming more characters from the string 
(repeating characters) or more characters from the pattern (the * matching 0 characters). If we get to the end of the 
string and there is still a pattern remaining, discard any * sets. The regex is a match if at the end the string and 
pattern are equal.
"""

import functools


@functools.lru_cache()
def is_match(s, p):
    if s == p:
        return True
    elif s and not p:
        return False
    elif not s:
        return is_match(s, p[:-2]) if len(p) >= 2 and p[-1] == '*' else False

    if s[-1] == p[-1] or p[-1] == '.':
        # simple match
        return is_match(s[:-1], p[:-1])
    elif p[-1] == '*':
        if p[-2] != s[-1] and p[-2] != '.':
            # no match, but * after
            return is_match(s, p[:-2])
        else:
            # match, with * after
            for idx in range(1, len(s)+1):
                # examine if consuming more string characters leads to a match
                if s[-idx] != s[-1] and p[-2] != '.':
                    break
                if is_match(s[:-idx], p):
                    return True
            # examine if skipping the pattern leads to a match
            return is_match(s, p[:-2])
    else:
        # no match, no * after
        return False


assert is_match('a', 'ab*') is True
assert is_match('abc', 'abc') is True
assert is_match('aa', 'a') is False
assert is_match('aab', 'c*aab') is True
assert is_match('aa', 'a*') is True
assert is_match('ab', '.*') is True
assert is_match('ab', '.*c') is False
assert is_match('aab', 'c*a*b') is True
assert is_match('mississippi', 'mis*is*p*.') is False
assert is_match('a', 'a*a') is True
assert is_match('bbbba', '.*a*a') is True
assert is_match('a', '.*..a*') is False
assert is_match('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c') is False
assert is_match('aa', 'ab*a*') is True
