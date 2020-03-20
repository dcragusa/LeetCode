"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length. Do not
allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.

Example 2:
Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means modification to the input array will be known to the
caller as well.

Internally you can think of this:
// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);
// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

"""
Similar to Problem 26, we cannot use a range if we are manipulating the index during the loop, so we use an infinite 
loop and manually break when the index gets to the size of the list.
"""


def remove_element(nums, val):
    idx = 0
    while True:
        if idx == len(nums):
            return idx
        elif nums[idx] == val:
            del nums[idx]
            idx -= 1
        idx += 1


nums = [3, 2, 2, 3]
assert remove_element(nums, 3) == 2
assert nums == [2, 2]

nums = [0, 1, 2, 2, 3, 0, 4, 2]
assert remove_element(nums, 2) == 5
assert nums == [0, 1, 3, 0, 4]
