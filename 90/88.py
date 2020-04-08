"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space  to hold additional elements from nums2.

Example:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3,  Output: [1,2,2,3,5,6]
"""

"""
We initialise two pointers to the start of each array. If the val of nums1 is larger than the val of nums2, we insert
the val of nums2 into the current position of nums1, and pop a 0 off the end of nums1 to maintain the appropriate 
length for nums1. We must also check that the nums1 pointer is not beyond m + the current index of nums2. This would 
mean that nums1 is pointing to a padding 0 and the remaining vals of nums2 must be inserted.
"""


def merge(nums1, m, nums2, n):
    nums1_idx = nums2_idx = 0
    while nums1_idx < m + n and nums2_idx < n:
        if nums1_idx >= m + nums2_idx or nums1[nums1_idx] > nums2[nums2_idx]:
            nums1.insert(nums1_idx, nums2[nums2_idx])
            nums1.pop()
            nums2_idx += 1
        nums1_idx += 1


nums = [1, 2, 3, 0, 0, 0]
merge(nums, 3, [2, 5, 6], 3)
assert nums == [1, 2, 2, 3, 5, 6]

nums = [1]
merge(nums, 1, [], 0)
assert nums == [1]

nums = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
merge(nums, 6, [1, 2, 2], 3)
assert nums == [-1, 0, 0, 1, 2, 2, 3, 3, 3]
