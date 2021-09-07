"""
Given an array words and a width max_width, format the text such that each line has exactly max_width characters
and is fully (left and right) justified. You should pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.
The last line of text should be left justified, with no extra space inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed max_width.
The input array words contains at least one word.

Example 1:
Input:
words = ['This', 'is', 'an', 'example', 'of', 'text', 'justification.'], maxWidth = 16
Output: ['This    is    an',
         'example  of text',
         'justification.  ']

Example 2:
Input:
words = ['What', 'must', 'be', 'acknowledgment', 'shall', 'be'], maxWidth = 16
Output: ['What   must   be',
         'acknowledgment  ',
         'shall be        ']
Explanation: Note that the last line is 'shall be    ' instead of 'shall     be',
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.

Example 3:
Input:
words = ['Science', 'is', 'what', 'we', 'understand', 'well', 'enough', 'to', 'explain',
         'to', 'a', 'computer.', 'Art', 'is', 'everything', 'else', 'we', 'do'], maxWidth = 20
Output: ['Science  is  what we',
         'understand      well',
         'enough to explain to',
         'a  computer.  Art is',
         'everything  else  we',
         'do                  ']
"""

"""
We iterate over the list of words, keeping track of the current length of the line. If the length becomes greater 
than max_width, we process the words visited up to that point. Processing is as follows: we calculate the number of 
spaces we need in the line (max_width minus the current length). Then we add the spaces already present (the number 
of words minus 1). If there is only one word, all the spaces go on the end. Otherwise, we divmod the spaces to obtain 
the quotient, which evenly spaces them out between the words, and a remainder. Then we go through the words adding 
the requisite quotient no. of spaces in between, and a remainder if present. We decrease the remainder as we go. 
The final line is appended left-justified.
"""


def process_line(words, length, max_width):
    if len(words) == 1:
        return words[0] + ' ' * (max_width - length)
    spaces = max_width - length + len(words) - 1
    quotient, remainder = divmod(spaces, len(words)-1)
    output = ''
    for word in words:
        output += word + ' ' * quotient
        if remainder:
            output += ' '
            remainder -= 1
    return output.rstrip()


def full_justify(words, max_width):
    output = []
    length, last_idx = 0, 0
    for idx, word in enumerate(words):
        length += len(word) if not length else len(word) + 1
        if length > max_width:
            output.append(process_line(words[last_idx:idx], length - 1 - len(word), max_width))
            length, last_idx = len(word), idx
    if length:
        output.append(' '.join(words[last_idx:]) + ' ' * (max_width - length))
    return output


assert full_justify([
    'This', 'is', 'an', 'example', 'of', 'text', 'justification.'
], 16) == ['This    is    an',
           'example  of text',
           'justification.  ']

assert full_justify([
    'What', 'must', 'be', 'acknowledgment', 'shall', 'be'
], 16) == ['What   must   be',
           'acknowledgment  ',
           'shall be        ']

assert full_justify([
    'Science', 'is', 'what', 'we', 'understand', 'well', 'enough', 'to', 'explain',
    'to', 'a', 'computer.', 'Art', 'is', 'everything', 'else', 'we', 'do'
], 20) == ['Science  is  what we',
           'understand      well',
           'enough to explain to',
           'a  computer.  Art is',
           'everything  else  we',
           'do                  ']
