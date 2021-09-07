"""
Given a string s consisting of upper/lower-case alphabets and empty space characters ' ', return the length of the last
word in the string. If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:
Input: "Hello World",  Output: 5
"""

"""
Fairly trivial, we just have to strip any whitespace from the end to make sure we end with a word, then use str.rfind 
to find the index of the rightmost space. We then return the length of the string - this index - 1 (the space itself).
"""


def length_of_last_word(s):
    s = s.rstrip()
    return len(s) - s.rfind(' ') - 1


assert length_of_last_word(' ') == 0
assert length_of_last_word('a ') == 1
assert length_of_last_word('Hello World') == 5
