"""
Implement next_permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must be rearranged as the lowest possible order
(i.e. sorted in ascending order). The replacement must be in-place and use only constant extra memory.

Here are some examples:
[1, 2, 3] → [1, 3, 2]      [3, 2, 1] → [1, 2, 3]      [1, 1, 5] → [1, 5, 1]
"""

"""
We iterate across the list right to left, looking for the first number that is smaller than the last. When we find 
the first smaller number, we must swap it with the smallest rightmost number that is larger than it. Because all 
numbers up until that point were in increasing order leftwards, we must sort the remaining part of the array to get 
them in increasing order rightwards. This produces the next smallest number. 
If there are no smaller numbers, that means there is no possible arrangement and the array must be sorted.
"""


def next_permutation(nums):
    len_nums = len(nums)
    if len_nums <= 1:
        return
    for idx in range(len_nums - 2, -1, -1):
        if (num := nums[idx]) < nums[idx + 1]:
            for smallest_increase_idx in range(len_nums - 1, -1, -1):
                if nums[smallest_increase_idx] > num:
                    nums[idx], nums[smallest_increase_idx] = nums[smallest_increase_idx], num
                    nums[idx + 1:] = reversed(nums[idx + 1:])
                    return
    nums.sort()


n = [1, 2, 3]
next_permutation(n)
assert n == [1, 3, 2]

n = [3, 2, 1]
next_permutation(n)
assert n == [1, 2, 3]

n = [1, 1, 5]
next_permutation(n)
assert n == [1, 5, 1]

n = [1, 2, 3, 2, 3]
next_permutation(n)
assert n == [1, 2, 3, 3, 2]

n = [1, 3, 2]
next_permutation(n)
assert n == [2, 1, 3]

n = [1, 1, 5, 4, 2]
next_permutation(n)
assert n == [1, 2, 1, 4, 5]
