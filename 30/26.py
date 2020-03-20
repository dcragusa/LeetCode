"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new
length. Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
extra memory. The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4
respectively.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means modification to the input array will be known to the
caller as well.

Internally you can think of this:
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);
// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

"""
We cannot use a range if we are manipulating the index during the loop, so we use an infinite loop and manually break
when the index gets to the size of the list. 
"""


def remove_duplicates(nums):
    prev = object()
    idx = 0
    while True:
        if idx == len(nums):
            return idx
        elif (num := nums[idx]) != prev:
            prev = num
        else:
            del nums[idx]
            idx -= 1
        idx += 1


nums = [1, 2]
assert remove_duplicates(nums) == 2
assert nums == [1, 2]

nums = [1, 1, 2]
assert remove_duplicates(nums) == 2
assert nums == [1, 2]

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
assert remove_duplicates(nums) == 5
nums = [0, 1, 2, 3, 4, 5]
