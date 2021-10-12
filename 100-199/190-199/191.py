"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (a.k.a. the Hamming weight).

Example 1:
Input: n = 00000000000000000000000000001011,  Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: n = 00000000000000000000000010000000,  Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: n = 11111111111111111111111111111101,  Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
"""


def hamming_weight(n):
    return bin(n).count('1')


assert hamming_weight(11) == 3
assert hamming_weight(128) == 1
assert hamming_weight(4294967293) == 31