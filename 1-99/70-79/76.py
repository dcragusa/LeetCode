"""
Given strings S and T, find the minimum window in S which contains all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC",  Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such a window, you are guaranteed that there will always be only one unique minimum window in S.
"""

"""
We first set up a counter of characters in T. We then use a sliding window over S: we check if a character is present
in T, and if so we decrement the appropriate counter. When all the counters are 0 (i.e. we have a valid substring), 
we proceed to pop characters off from the beginning of the substring. When we pop off a character from T, we have
found a local minimum substring and update min_substring if it is smaller.
"""


from collections import Counter, deque


def min_window(s, t):
    t_counter = Counter(t)
    num_t_chars_in_window, num_t_chars = 0, len(t_counter)
    min_substring, current_substring = '', deque()
    for char in s:
        if num_t_chars_in_window < num_t_chars:
            if char in t_counter:
                t_counter[char] -= 1
                if t_counter[char] == 0:
                    num_t_chars_in_window += 1
            current_substring.append(char)
        while num_t_chars_in_window == num_t_chars:
            discarded = current_substring.popleft()
            if discarded in t_counter:
                if t_counter[discarded] == 0:
                    if not min_substring or len(current_substring) + 1 < len(min_substring):
                        min_substring = discarded + ''.join(current_substring)
                    num_t_chars_in_window -= 1
                t_counter[discarded] += 1
    return min_substring


assert min_window('ADOBECODEBANC', 'ABC') == 'BANC'
assert min_window('ADOBECODEBANC', 'ABCF') == ''
