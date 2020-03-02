"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
We iterate over the string, keeping a dict mapping of char: idx for O(1) lookups. The substring length will be the 
difference between the current index and the index of the start of the substring (0 at start). If we find a double, 
the start of the substring is set to the index of the last time that character was found (thus eliminating the first
character of that double from the substring).
"""


def length_of_longest_substring(s):
    indices = {}
    substring_idx = longest_substring = 0

    for idx, char in enumerate(s):
        if char in indices and (new_substring_idx := indices[char] + 1) > substring_idx:
            substring_idx = new_substring_idx
        indices[char] = idx
        if (substring_length := idx - substring_idx + 1) > longest_substring:
            longest_substring = substring_length

    return longest_substring


assert length_of_longest_substring('abcabcbb') == 3
assert length_of_longest_substring('bbbbb') == 1
assert length_of_longest_substring('pwwkew') == 3
assert length_of_longest_substring('abba') == 2
assert length_of_longest_substring(' ') == 1
assert length_of_longest_substring('') == 0
