"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:
- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure, it can be matched later.
- bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
  word may contain dots '.' where dots can be matched with any letter.

Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary word_dict = new WordDictionary();
word_dict.addWord("bad");
word_dict.addWord("dad");
word_dict.addWord("mad");
word_dict.search("pad"); // return False
word_dict.search("bad"); // return True
word_dict.search(".ad"); // return True
word_dict.search("b.."); // return True
"""

"""
We can solve this in a couple of ways: one is to leverage regex search that has dot matching built in. We separate the
strings by string length to improve performance, as regex can be quite slow given a large search space. Another way
is by implementing a trie similar to that in problem 208: if we encounter a dot, we must search through all children
of a given node. We do this by implementing a function that searches from a given node and index of the string, instead
of from the root. We can implement some space savings by using __slots__ on the TrieNode class, which will be created 
many times in the trie solution.
"""


# import re
# from collections import defaultdict
#
#
# class WordDictionary:
#
#     def __init__(self):
#         self.words = defaultdict(str)
#
#     def addWord(self, word):
#         self.words[len(word)] += f'#{word}#'
#
#     def search(self, word):
#         return bool(re.search(f'#{word}#', self.words[len(word)]))


class TrieNode:
    __slots__ = ['terminating', 'children']

    def __init__(self):
        self.terminating = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.word = None

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.terminating = True

    def search_from_node(self, node, index):
        if index == len(self.word):
            return node.terminating
        char = self.word[index]
        if char == '.':
            return any(self.search_from_node(child, index+1) for child in node.children.values())
        if char not in node.children:
            return False
        return self.search_from_node(node.children[char], index+1)

    def search(self, word):
        self.word = word
        return self.search_from_node(self.root, 0)


word_dict = WordDictionary()
word_dict.addWord("bad")
word_dict.addWord("dad")
word_dict.addWord("mad")
assert word_dict.search("pad") is False
assert word_dict.search("bad") is True
assert word_dict.search(".ad") is True
assert word_dict.search("b..") is True
