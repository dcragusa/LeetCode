"""
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],  Output: [["ate","eat","tea"], ["nat","tan"], ["bat"]]

Note:
All inputs will be in lowercase. The order of your output does not matter.
"""

"""
Firstly we sort each string in the given array - this will allow us to make direct comparisons for anagrams. We then
append each string to a defaultdict with the key being the sorted string. Finally, we return the values of the dict.
"""


from collections import defaultdict


def group_anagrams(strs):
    anagrams = defaultdict(list)
    for idx, sorted_strs in enumerate(map(lambda x: ''.join(sorted(x)), strs)):
        anagrams[sorted_strs].append(strs[idx])
    return list(anagrams.values())


assert group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
