"""
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If
the array contains less than two elements, return 0. You must write an algorithm that runs in linear time and uses
linear extra space.

Example 1:
Input: nums = [3, 6, 9, 1],  Output: 3
Explanation: The sorted form of the array is [1, 3, 6, 9], either (3, 6) or (6, 9) has the maximum difference 3.

Example 2:
Input: nums = [10],  Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
"""

"""
The naive solution to this would be to sort the array, then simply iterate across, keeping track of the max gap (also
faster for reasonable size inputs, given how optimised the Python sort and how simple the iteration are).
The challenge in this lies in getting the 'sorting' behaviour in linear time. We can take advantage of bucket sorting.
Firstly, we establish the minimum and maximum numbers of the array (both achievable in O(n) time). We know the step
between these buckets must be between 1 and the difference between max and min numbers divided by the size of nums.
We then create enough buckets across the max - min range of numbers so that one bucket is guaranteed to be empty, and
initialise these buckets to + and - infinity. We then go through nums and assign each number to a bucket, updating the
bucket's minimum and maximums if necessary.
We then go through the buckets and compare the gaps between buckets, excluding the buckets with + and - infinity. We 
are guaranteed that the gaps within the buckets are going to be smaller than the gaps between the buckets, so the
largest of these will be the maximum gap.
This is all in linear time because we don't actually care about the sorting of numbers within the buckets themselves
(if we did, the complexity would be worse). 
"""


# def maximum_gap_naive(nums):
#     if len(nums) < 2:
#         return 0
#     nums.sort()
#     prev = nums[0]
#     max_gap = 0
#     for num in nums[1:]:
#         max_gap = max(max_gap, abs(num - prev))
#         prev = num
#     return max_gap


def maximum_gap(nums):
    if len(nums) < 2:
        return 0

    min_num, max_num = min(nums), max(nums)

    step = max(1, (max_num - min_num) // (len(nums)-1))
    num_buckets = ((max_num - min_num) // step) + 1   # one additional bucket
    buckets = [[float('inf'), float('-inf')] for _ in range(num_buckets)]

    for num in nums:
        bucket_idx = (num - min_num) // step
        bucket_min, bucket_max = buckets[bucket_idx]
        buckets[bucket_idx] = min(bucket_min, num), max(bucket_max, num)

    max_gap = 0
    prev_num = min_num
    for bucket_min, bucket_max in buckets:
        if bucket_min != float('inf'):
            max_gap = max(max_gap, bucket_min - prev_num)
            prev_num = bucket_max
    return max_gap


assert maximum_gap([1, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 8
assert maximum_gap([1, 5, 2, 4, 3]) == 1
assert maximum_gap([3, 6, 9, 1]) == 3
assert maximum_gap([10]) == 0
