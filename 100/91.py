"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1, 'B' -> 2, ... 'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: "12",  Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226",  Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

"""
We set up a set of valid mappings for O(1) access. We then proceed to recursively examine the string: the number of
ways to decode is num_decodings(s[1:]) + num_decodings(s[:2]) * num_decodings(s[2:]). We special case decodings of 1/2
characters. We cache the results, and further optimisation can be obtained by only calculating num_decodings(s[2:])
only when s[:2] is valid.
"""


from functools import lru_cache

valid_chars = {str(i) for i in range(1, 27)}


@lru_cache()
def decodable(s):
    return int(s in valid_chars)


@lru_cache()
def num_decodings(s):
    if s[0] == '0':
        return 0
    elif len(s) == 1:
        return 1
    if len(s) == 2:
        return decodable(s) + int(s[1] != '0')
    decodings = num_decodings(s[1:])
    if prefix := decodable(s[:2]):
        decodings += prefix * num_decodings(s[2:])
    return decodings


assert num_decodings('0') == 0
assert num_decodings('00') == 0
assert num_decodings('10') == 1
assert num_decodings('12') == 2
assert num_decodings('226') == 3
assert num_decodings('111') == 3
assert num_decodings('2321') == 4
assert num_decodings('232123212321232123212321232123212321232123212321232123212321232') == 61035156250

