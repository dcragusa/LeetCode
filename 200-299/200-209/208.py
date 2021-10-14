"""
A trie (pronounced as 'try') or prefix tree is a tree data structure used to efficiently store and retrieve keys in a
dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false
  otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix
  prefix, and false otherwise.

Example 1:
Input
['Trie', 'insert', 'search', 'search', 'startsWith', 'insert', 'search']
[[], ['apple'], ['apple'], ['app'], ['app'], ['app'], ['app']]
Output
[None, None, True, False, True, None, True]

Explanation
Trie trie = new Trie();
trie.insert('apple');
trie.search('apple');   // return True
trie.search('app');     // return False
trie.startsWith('app'); // return True
trie.insert('app');
trie.search('app');     // return True
"""

"""
We implement a TrieNode class that has the node character, a dictionary of children, and a terminating flag. In the
main Trie class, we start with a dummy TrieNode root. When inserting a word, we start off with the node being the root,
then iterate over each character and see if the character is present in the current node. If not, we create a TrieNode
and add it to the current node's children. We then set the current node to be the found (or created) TrieNode and go
to the next character. We set the last node's terminating flag to True to indicate that a complete word ends at this 
node. To implement search, the procedure is quite similar - we check if each character is in the node's children and go 
downwards. If any character is not found in the node's children, we return False. The last node's terminating flag must 
also be True. The prefix search is identical except the terminating flag is not checked at the end of the search.
"""


class TrieNode:
    def __init__(self, val):
        self.val = val
        self.terminating = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.terminating = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.terminating

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


trie = Trie()
trie.insert('apple')
assert trie.search('apple') is True
assert trie.search('app') is False
assert trie.startsWith('app') is True
trie.insert('app')
assert trie.search('app') is True
