"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3, 2, 3],  Output: [3]

Example 2:
Input: nums = [1],  Output: [1]

Example 3:
Input: nums = [1, 2],  Output: [1, 2]
"""

"""
We follow the same logic from 169: we can solve this trivially with Counter in O(n) time but also O(n) space. 
Alternatively, we can extend the Boyer-Moore voting algorithm logic to keep track of two variables. We have to perform
another pass over nums to verify that the candidates are present more than the required number of times.
"""

from collections import Counter


def majority_element_counter(nums):
    return [i[0] for i in Counter(nums).items() if i[1] > len(nums)//3]


def majority_element_boyer_moore(nums):
    candidate_1, candidate_2, count_1, count_2 = None, None, 0, 0
    for num in nums:
        if num == candidate_1:
            count_1 += 1
        elif num == candidate_2:
            count_2 += 1
        elif not count_1:
            candidate_1, count_1 = num, 1
        elif not count_2:
            candidate_2, count_2 = num, 1
        else:
            count_1 -= 1
            count_2 -= 1

    count_1, count_2 = 0, 0
    for num in nums:
        if num == candidate_1:
            count_1 += 1
        elif num == candidate_2:
            count_2 += 1

    results = []
    if count_1 > len(nums) // 3:
        results.append(candidate_1)
    if count_2 > len(nums) // 3:
        results.append(candidate_2)
    return results


assert majority_element_counter([3, 2, 3]) == majority_element_boyer_moore([3, 2, 3]) == [3]
assert majority_element_counter([1]) == majority_element_boyer_moore([1]) == [1]
assert majority_element_counter([1, 2]) == majority_element_boyer_moore([1, 2]) == [1, 2]
assert majority_element_counter([1, 1, 3, 1, 4, 5, 6]) == majority_element_boyer_moore([1, 1, 3, 1, 4, 5, 6]) == [1]
