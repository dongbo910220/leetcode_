'''
https://leetcode.com/problems/map-sum-pairs/
'''


class TrieNode():
    def __init__(self, count=0):
        self.count = count
        self.children = {}


class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.keys = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        node = self.root
        delta = val - self.keys.get(key, 0)
        self.keys[key] = val

        node.count += delta
        for letter in key:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
            node.count += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return 0
            node = node.children[letter]
        return node.count

'''
Success
Details 
Runtime: 20 ms, faster than 79.86% of Python online submissions for Map Sum Pairs.
Memory Usage: 12.7 MB, less than 97.62% of Python online submissions for Map Sum Pairs.
'''