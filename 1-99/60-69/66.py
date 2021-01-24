"""
Given a non-empty array of digits representing a non-negative integer, add one to the integer. The digits are stored
such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3],  Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1],  Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

"""
We iterate backwards through the array. If the existing digit is not a 9, we can add one and return. If it is a 9, we
must carry one over to the next digit along. If the very last number is a 9 as well, we must prepend a 1 to the array.
"""


def add_one(digits):
    for idx in range(len(digits)-1, -1, -1):
        if digits[idx] != 9:
            digits[idx] += 1
            return digits
        else:
            digits[idx] = 0
            if idx == 0:
                return [1] + digits


assert add_one([1, 2, 3]) == [1, 2, 4]
assert add_one([4, 3, 2, 1]) == [4, 3, 2, 2]
assert add_one([1, 9]) == [2, 0]
assert add_one([9, 9, 9]) == [1, 0, 0, 0]
