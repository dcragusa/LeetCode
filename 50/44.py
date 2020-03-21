"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:
Input:, s = "aa", p = "a", Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa", p = "*", Output: true
Explanation: '*' matches any sequence.

Example 3:
Input:
s = "cb", p = "?a", Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input:
s = "adceb", p = "*a*b", Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input:, s = "acdcb", p = "a*c?b", Output: false
"""

"""
Somewhat similar to 10, made easier by the fact every single letter in p must appear in s. We can match any non-* 
characters at each end of s and p straight away. We can then check if every pattern fragment (groups of letters in p)
exists in s in order (this cuts down on a lot of backtracking for multiple * in p). Finally, if we find a * we must
check whether matching any number of characters in s leads to a solution.
"""


def is_match(s, p):
    if s == p:
        return True
    elif s and not p:
        return False
    elif not s:
        return all(map(lambda x: x == '*', p))

    first_s, last_s, first_p, last_p = s[0], s[-1], p[0], p[-1]
    if first_s == first_p or first_p == '?':
        # simple match
        return is_match(s[1:], p[1:])
    elif last_s == last_p or last_p == '?':
        # simple match
        return is_match(s[:-1], p[:-1])
    elif (first_s != first_p and first_p != '*') or (last_s != last_p and last_p != '*'):
        # no match
        return False

    # check if all pattern fragments are in the string
    s_idx = 0
    for pattern_fragment in p.replace('?', '*').split('*'):
        idx = s.find(pattern_fragment, s_idx)
        if idx == -1:
            return False
        s_idx = idx + len(pattern_fragment)

    if first_p == '*':
        # examine if consuming more string characters leads to a match
        # there must be at least len(s) non-wildcard chars in the pattern
        return (len(s) > len(p) - p.count('*') - 1) and any(is_match(s[idx:], p[1:]) for idx in range(len(s)+1))
    else:
        return False


assert is_match('aa', 'a') is False
assert is_match('aa', '*') is True
assert is_match('ab', '?*') is True
assert is_match('cb', '?a') is False
assert is_match('adceb', '*a*b') is True
assert is_match('acdcb', 'a*c?b') is False
assert is_match('mississippi', 'm??*ss*?i*pi') is False
assert is_match('abefcdgiescdfimde', 'ab*cd?i*de') is True
assert is_match('aaaababbbaaabaabbbbabaababaabbabbaabababbaaaaaaabba', 'baaaaba*****b***ab******') is False
assert is_match(
    'abaabaaaabbabbaaabaabababbaabaabbabaaaaabababbababaabbabaabbbbaabbbbbbbabaaabbaaaaabbaabbbaaaaabbbabb',
    'ab*aaba**abbaaaa**b*b****aa***a*b**ba*a**ba*baaa*b*ab*') is False
