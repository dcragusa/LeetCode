"""
You are given a sorted unique integer array nums. Return the smallest sorted list of ranges that cover all the numbers
in the array exactly. That is,  each element of nums is covered by exactly one of the ranges, and there is no integer x
such that x is in one of the ranges but not in nums.
Each range [a, b] in the list should be output as: 'a->b' if a != b, 'a' if a == b

Example 1:
Input: nums = [0, 1, 2, 4, 5, 7],  Output: ['0->2', '4->5', '7']

Example 2:
Input: nums = [0, 2, 3, 4, 6, 8, 9],  Output: ['0', '2->4', '6', '8->9']

Example 3:
Input: nums = [],  Output: []

Example 4:
Input: nums = [-1],  Output: ['-1']

Example 5:
Input: nums = [0],  Output: ['0']
"""

"""
We go through nums keeping track of the start and end of the current range using variables a and b. If a is None, we
assign num to a. If the number is consecutive, then we either assign it to b if b is None, or replace b (as the range
has grown). If the number is no longer consecutive, we add the current range to the output.
"""


def summary_ranges(nums):
    a, b = None, None
    output = []

    def process_output():
        nonlocal a, b
        if a is None:
            return
        output.append(str(a) if b is None else f'{a}->{b}')
        a = b = None

    for num in nums:
        if a is None:
            a = num
        elif b is None and num == a + 1:
            b = num
        elif b is not None and num == b + 1:
            b = num
        else:
            process_output()
            a = num
    process_output()

    return output


assert summary_ranges([0, 1, 2, 4, 5, 7]) == ['0->2', '4->5', '7']
assert summary_ranges([0, 2, 3, 4, 6, 8, 9]) == ['0', '2->4', '6', '8->9']
assert summary_ranges([]) == []
assert summary_ranges([-1]) == ['-1']
assert summary_ranges([0]) == ['0']
