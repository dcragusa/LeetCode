"""
Given two version numbers, version1 and version2, compare them. Version numbers consist of one or more revisions
joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at
least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the
next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.
To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their
integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version
number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than
version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:
If version1 < version2, return -1. If version1 > version2, return 1. Otherwise, return 0.

Example 1:
Input: version1 = '1.01', version2 = '1.001',  Output: 0
Explanation: Ignoring leading zeroes, both '01' and '001' represent the same integer '1'.

Example 2:
Input: version1 = '1.0', version2 = '1.0.0',  Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as '0'.

Example 3:
Input: version1 = '0.1', version2 = '1.1',  Output: -1
Explanation: version1's revision 0 is '0', while version2's revision 0 is '1'. 0 < 1, so version1 < version2.

Example 4:
Input: version1 = '1.0.1', version2 = '1',  Output: 1

Example 5:
Input: version1 = '7.5.2.4', version2 = '7.5.3',  Output: -1
"""

"""
Pretty easy, we just split the version into integer parts, then iterate with zip_longest to provide the necessary 0
values if missing.
"""

from itertools import zip_longest


def compare_version(version1, version2):
    split1 = [int(part) for part in version1.split('.')]
    split2 = [int(part) for part in version2.split('.')]
    for part1, part2 in zip_longest(split1, split2, fillvalue=0):
        if part1 < part2:
            return -1
        elif part1 > part2:
            return 1
    return 0


assert compare_version('1.01', '1.001') == 0
assert compare_version('1.0', '1.0.0') == 0
assert compare_version('0.1', '1.1') == -1
assert compare_version('1.0.1', '1') == 1
assert compare_version('7.5.2.4', '7.5.3') == -1
