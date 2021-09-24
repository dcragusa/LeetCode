"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100, 4, 200, 1, 3, 2],  Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],  Output: 9
"""

"""
We first convert nums to a set for O(1) lookups (also eliminating duplicates). Then we iterate across this set - for 
each number, we check whether consecutive numbers both lower and higher are present in the set to establish the size
of the run of consecutive elements. We add numbers encountered to another set of seen numbers to avoid double counting.
"""


def longest_consecutive(nums):
    num_set = set(nums)
    seen = set()
    longest_run = 0
    for num in num_set:
        if num in seen:
            continue
        seen.add(num)
        run = 1
        dec, inc = num - 1, num + 1
        while dec in num_set:
            seen.add(dec)
            run += 1
            dec -= 1
        while inc in num_set:
            seen.add(inc)
            run += 1
            inc += 1
        longest_run = max(longest_run, run)
    return longest_run


assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
