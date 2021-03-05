'''
https://leetcode.com/problems/add-and-search-word-data-structure-design/
'''


class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isword = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            node = node.children[c]
        node.isword = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        if not word:
            if node.isword:
                self.res = True
            return
        if word[0] == '.':
            for node2 in node.children.values():
                self.dfs(node2, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])

'''
Success
Details 
Runtime: 416 ms, faster than 46.97% of Python online submissions for Add and Search Word - Data structure design.
Memory Usage: 37.1 MB, less than 29.88% of Python online submissions for Add and Search Word - Data structure design.
'''