"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""

"""
We iterate through s3 and see if we can match a character from s1 or s2. We then recur with s1, s2 and s3 minus the
appropriate characters. We have 3 possible outcomes: 1) we exhaust all of s1, s2 and s3. This means that an interleave
is possible and so we return True. 2) we exhaust s3 but there are still characters remaining in s1 or s2. This means
that an interleave was not possible with the letter choices, so we return False. 3) Neither s1 nor s2's first chars
are a match for s3. This means that like 2, an interleave was not possible.
"""


from functools import lru_cache


@lru_cache()
def is_interleave(s1, s2, s3):

    if s1 == s2 == s3 == '':
        return True
    elif (s1 or s2) and not s3:
        return False

    if s1 and s1[0] == s3[0] and is_interleave(s1[1:], s2, s3[1:]):
        return True
    if s2 and s2[0] == s3[0] and is_interleave(s1, s2[1:], s3[1:]):
        return True
    return False


assert is_interleave('aabcc', 'dbbca', 'aadbbcbcac') is True
assert is_interleave('aabcc', 'dbbca', 'aadbbbaccc') is False
assert is_interleave('bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbb'
                     'ababbbbbabbbbababbabaabababbbaabababababbbaaababaa',
                     'babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaab'
                     'aaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab',
                     'babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabb'
                     'baaaaabbbbaabbaaabababbaaaaaabababbababaababbababb'
                     'bababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababa'
                     'ababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab') is False
