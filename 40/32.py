"""
Given a string containing just the characters '(' and ')', find the length of the longest valid parentheses substring.

Example 1:
Input: "(()", Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())", Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""

"""
We go across the string, adding open brackets to a stack. If we find a closed bracket, we pop the last open bracket off
the stack to make a valid substring. If this substring is next to another valid substring, we can merge them to make
another valid substring (by keeping track of existing substrings via a last-to-first index mapping).
"""


def longest_valid_parentheses(s):
    open_bracket_idxs, last_to_first_valid_substrings = [], {}
    longest_valid_substring, current_valid_substring = 0, 0
    for idx, char in enumerate(s):
        if char == '(':
            open_bracket_idxs.append(idx)
        elif open_bracket_idxs:
            idx_last_open_bracket_matched = open_bracket_idxs.pop()
            if (last_char_of_a_substring := idx_last_open_bracket_matched-1) in last_to_first_valid_substrings:
                start_of_the_substring = last_to_first_valid_substrings[last_char_of_a_substring]
            else:
                start_of_the_substring = idx_last_open_bracket_matched
            last_to_first_valid_substrings[idx] = start_of_the_substring
            current_valid_substring = idx - start_of_the_substring + 1
        longest_valid_substring = max(longest_valid_substring, current_valid_substring)

    return longest_valid_substring


assert longest_valid_parentheses('(()') == 2
assert longest_valid_parentheses(')()())') == 4
assert longest_valid_parentheses('(())()(()((') == 6
