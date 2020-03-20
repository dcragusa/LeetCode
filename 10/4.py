"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
"""

"""
The brute force solution is simple: we know what index the median has to be based on the combined length of the inputs.
Simply add to the array based on order until we get to that index. If the total length is odd, we know the median
is a single element so we can return the last element added. If the total length is even, we have to average the last
two elements added. Hence we only need to keep track of the last two elements of the combined sorted array.

The log complexity solution is a lot more complex: we split both arrays into two parts. Because the parts are 
already sorted, to find the median we just need the biggest number on the left side of nums1 to be smaller than the 
smallest number on the right side of nums2, and likewise we need the biggest number on the left side of nums2 to be 
smaller than the smallest number on the right side of nums1. If we select index i from nums1, we must select 
len1 + len2 + 1 // 2 - i from nums2 (this follows from the arrays being sorted). Then we do a binary search to find
i in nums1 until the above parameters are satisfied.
"""

# from itertools import count
# from collections import deque
#
#
# def median_two_sorted_arrays(nums1, nums2):
#     i = j = 0
#     len1, len2 = len(nums1), len(nums2)
#     arr = deque(maxlen=2)
#     odd = (len1 + len2) % 2
#     median_idx = (len1 + len2) // 2
#     for idx in count():
#         if j == len2:
#             arr.append(nums1[i])
#             i += 1
#         elif i == len1:
#             arr.append(nums2[j])
#             j += 1
#         elif nums1[i] <= nums2[j]:
#             arr.append(nums1[i])
#             i += 1
#         else:
#             arr.append(nums2[j])
#             j += 1
#
#         if idx == median_idx:
#             return arr[-1] if odd else (arr[-2] + arr[-1]) / 2


def median_two_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        # we want nums1 to be smaller
        nums1, nums2 = nums2, nums1

    len1, len2 = len(nums1), len(nums2)
    min_idx, max_idx = 0, len1

    while min_idx <= max_idx:
        i = (min_idx + max_idx) // 2
        j = (len1 + len2 + 1) // 2 - i
        if i < len1 and nums2[j-1] > nums1[i]:
            min_idx = i + 1
        elif i > 0 and nums1[i-1] > nums2[j]:
            max_idx = i - 1
        else:
            max_left1 = float('-inf') if i == 0 else nums1[i-1]
            max_left2 = float('-inf') if j == 0 else nums2[j-1]
            min_right1 = float('inf') if i == len1 else nums1[i]
            min_right2 = float('inf') if j == len2 else nums2[j]

            if max_left1 <= min_right2 and min_right1 >= max_left2:
                if (len1 + len2) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    return max(max_left1, max_left2)


assert median_two_sorted_arrays([1, 3], [2]) == 2
assert median_two_sorted_arrays([1, 2], [3, 4]) == 2.5
