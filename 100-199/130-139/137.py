"""
Given a non-empty array of integers nums, every element appears three times except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2, 2, 3, 2],  Output: 3

Example 2:
Input: nums = [0, 1, 0, 1, 0, 1, 99],  Output: 99
"""

"""
We still have to implement bitwise operators, but it is no longer as simple as 136. Now it is a 3-step process for 
each number. We set up two numbers initialised to zeros, ones and twos. First, we add the number to twos if it is in 
ones (we can use OR: | for this as we don't need to remove numbers from twos at any point). Second, we add to ones if 
it is not already present, and remove it if it is present (using XOR: ^). Finally, we remove bits common to  ones and 
twos, by taking the complement of common bits (using ~) and removing the bits from both ones and twos if present.
"""


def single_number(nums):
    ones = twos = 0
    for num in nums:
        # step 1: add to twos if in ones
        twos |= ones & num
        # step 2: add to ones if not present and remove if present
        ones ^= num
        # step 3: remove bits common to ones and twos
        common_bits = ~(ones & twos)
        ones &= common_bits
        twos &= common_bits
    return ones


assert single_number([2, 2, 3, 2]) == 3
assert single_number([0, 1, 0, 1, 0, 1, 99]) == 99
