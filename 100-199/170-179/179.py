"""
Given a list of non-negative integers nums, arrange them such that they form the largest number. The result may be
very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10, 2],  Output: '210'

Example 2:
Input: nums = [3, 30, 34, 5, 9],  Output: '9534330'

Example 3:
Input: nums = [1],  Output: '1'

Example 4:
Input: nums = [10],  Output: '10'
"""

"""
This is easy to do once we have the correct comparator to use to sort the array of nums. We take advantage of the fact
that if a~b > b~a and b~c > c~b, then a~c > c~a to write a comparison function that can be used in Python's default 
sort. Proof: https://leetcode.com/problems/largest-number/discuss/291988
"""

from functools import cmp_to_key


def cmp(a, b):
    if a + b > b + a:
        # greater than
        return 1
    if a + b < b + a:
        # less than
        return -1
    return 0


def largest_number(nums):
    nums = list(map(str, nums))
    largest_num = ''.join(sorted(nums, key=cmp_to_key(cmp), reverse=True))
    return '0' if largest_num[0] == '0' else largest_num


assert largest_number([10, 2]) == '210'
assert largest_number([3, 30, 34, 5, 9]) == '9534330'
assert largest_number([1]) == '1'
assert largest_number([10]) == '10'
assert largest_number([111, 211, 121, 112, 100, 110, 1, 11]) == '211121112111111110100'
assert largest_number([34323, 3432]) == '343234323'
