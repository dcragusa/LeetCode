"""
Given an integer array nums and two integers k and t, return true if there are two distinct indices i and j in the
array such that abs(i - j) <= k and abs(nums[i] - nums[j]) <= t.

Example 1:
Input: nums = [1, 2, 3, 1], k = 3, t = 0,  Output: True

Example 2:
Input: nums = [1, 0, 1, 1], k = 1, t = 2,  Output: True

Example 3:
Input: nums = [1, 5, 9, 1, 5, 9], k = 2, t = 3,  Output: False
"""

"""
This can be implemented using bucket sorting. We use an OrderedDict for fast pops to keep track of the index gap. Each
bucket is value gap wide - therefore, a number is within the value gap if it falls within the same bucket or in one of 
the neighouring buckets.
"""

from collections import OrderedDict


def contains_nearby_almost_duplicate(nums, index_gap, value_gap):
    bucket_dict = OrderedDict()
    window = value_gap + 1
    for num in nums:
        if len(bucket_dict) > index_gap:
            bucket_dict.popitem(last=False)
        bucket = num // window
        if (
            bucket in bucket_dict or
            (bucket - 1 in bucket_dict and abs(bucket_dict[bucket-1] - num) <= value_gap) or
            (bucket + 1 in bucket_dict and abs(bucket_dict[bucket+1] - num) <= value_gap)
        ):
            return True
        bucket_dict[bucket] = num
    return False


assert contains_nearby_almost_duplicate([1, 2, 3, 1], 3, 0) is True
assert contains_nearby_almost_duplicate([1, 0, 1, 1], 1, 2) is True
assert contains_nearby_almost_duplicate([1, 5, 9, 1, 5, 9], 2, 3) is False
assert contains_nearby_almost_duplicate([2, 0, -2, 2], 2, 1) is False
