"""
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in
this range, inclusive.

Example 1:
Input: left = 5, right = 7,  Output: 4

Example 2:
Input: left = 0, right = 0,  Output: 0

Example 3:
Input: left = 1, right = 2147483647,  Output: 0
"""

"""
One might think to repeatedly AND numbers in the range, but this might be more than a billion operations (as in example
3). Instead, we can realise that the bitwise AND of all numbers in the range inclusive is equivalent to finding the 
initial common bits (as all other bits will roll over to 0 while counting upwards to the number). We therefore convert
both numbers to binary strings, and if they are both the same length, count along both at the same time, adding the
common bits to a result string. When we find a mismatch, we pad the result string to have the same length as the inputs
and convert that to an integer to be returned.
"""


def range_bitwise_and(left, right):
    left_bit_str = bin(left)[2:]
    right_bit_str = bin(right)[2:]
    if len(left_bit_str) != len(right_bit_str):
        return 0

    common_bit_str = ''
    for left, right in zip(left_bit_str, right_bit_str):
        if left != right:
            break
        common_bit_str += left
    return int(common_bit_str.ljust(len(left_bit_str), '0'), 2)


assert range_bitwise_and(5, 7) == 4
assert range_bitwise_and(0, 0) == 0
assert range_bitwise_and(1, 2147483647) == 0
assert range_bitwise_and(1073741824, 2147483647) == 1073741824
assert range_bitwise_and(1992818688, 1995035968) == 1992294400
