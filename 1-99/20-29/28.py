"""
Implement str_str(). Return the index of the first occurrence of a substring (needle) in a string (haystack),
or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll", Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba", Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent with
C's strstr() and Java's indexOf().
"""

"""
This is batteries included in Python, as str.find(). An alternative implementation compares a sliding slice of length
len(needle).
"""


# def str_str(haystack, needle):
#     return haystack.find(needle)


def str_str(haystack, needle):
    l_hay, l_needle = len(haystack), len(needle)
    if not needle:
        return 0
    elif l_needle > l_hay:
        return -1
    for i in range(l_hay-l_needle+1):
        if haystack[i:i+l_needle] == needle:
            return i
    return -1


assert str_str('a', 'a') == 0
assert str_str('hello', 'll') == 2
assert str_str('aaaaa', 'bba') == -1
