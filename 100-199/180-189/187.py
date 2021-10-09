"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'. When studying DNA,
it is useful to identify repeated sequences within the DNA. Given a string s that represents a DNA sequence, return
all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer
in any order.

Example 1:
Input: s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT',  Output: ['AAAAACCCCC', 'CCCCCAAAAA']

Example 2:
Input: s = 'AAAAAAAAAAAAA',  Output: ['AAAAAAAAAA']
"""

"""
This one is pretty simple - we have a sliding window 10 characters wide, adding to a set of seen substrings to check
whether the substring occurs more than once.
"""


def find_repeated_dna_sequences(s):
    if len(s) < 11:
        return []
    seen = set()
    duplicated = set()
    for i in range(len(s)-9):
        substring = s[i:i+10]
        if substring in seen:
            duplicated.add(substring)
        seen.add(substring)
    return list(duplicated)


assert sorted(find_repeated_dna_sequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')) == ['AAAAACCCCC', 'CCCCCAAAAA']
assert find_repeated_dna_sequences('AAAAAAAAAAAAA') == ['AAAAAAAAAA']
assert find_repeated_dna_sequences('AAAAAAAAAAA') == ['AAAAAAAAAA']
