"""
Given an integer array nums and an integer k, return the kth largest element in the array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3, 2, 1, 5, 6, 4], k = 2,  Output: 5

Example 2:
Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4,  Output: 4
"""

"""
This can be trivially implemented by using Python's default sort and taking the kth element from the end of the array.
Alternatively we can implement this using a heap. Every time the heap exceeds k, we pop the minimum element - at the 
end we will be left with the k largest elements of the array, so the kth largest is the minimum in the heap.
"""

import heapq


# def find_kth_largest(nums, k):
#     return sorted(nums)[-k]


def find_kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappushpop(heap, num) if len(heap) == k else heapq.heappush(heap, num)
    return heapq.heappop(heap)


assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
