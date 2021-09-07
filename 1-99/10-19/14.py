"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower", "flow", "flight"],  Output: "fl"

Example 2:
Input: ["dog", "racecar", "car"],  Output: ""
Explanation: There is no common prefix among the input strings.

Note: All given inputs are in lowercase letters a-z.
"""

"""
First we find the shortest string present in the array: the prefix has to be part of or equal to this. Then we iterate
through this string: if any strings in the array do not have the same character as the shortest string at the same 
index, we stop the iteration and have found the longest common prefix.
"""


def longest_common_prefix(strs):
    shortest_str = None
    for s in strs:
        if shortest_str is None or len(s) < len(shortest_str):
            shortest_str = s
    if shortest_str is None:
        return ''
    for i in range(len(shortest_str)):
        if any(s[i] != shortest_str[i] for s in strs):
            return shortest_str[:i]
    return shortest_str


assert longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'
assert longest_common_prefix(['dog', 'racecar', 'car']) == ''
assert longest_common_prefix(['a']) == 'a'
assert longest_common_prefix(['', 'b']) == ''
