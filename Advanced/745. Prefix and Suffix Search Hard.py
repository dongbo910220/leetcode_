'''
https://leetcode.com/problems/prefix-and-suffix-search/
'''

class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        from collections import defaultdict
        self.prefixes = defaultdict(set)
        self.suffixes = defaultdict(set)
        self.weights = {}
        for index, word in enumerate(words):
            prefix, suffix = '', ''
            for char in [''] + list(word):
                prefix += char
                self.prefixes[prefix].add(word)
            for char in [''] + list(word[::-1]):
                suffix += char
                self.suffixes[suffix[::-1]].add(word)
            self.weights[word] = index

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        weight = -1
        # print(self.suffixes)
        for word in self.prefixes[prefix] & self.suffixes[suffix]:
            if self.weights[word] > weight:
                weight = self.weights[word]
        return weight

'''
Success
Details 
Runtime: 692 ms, faster than 79.66% of Python online submissions for Prefix and Suffix Search.
Memory Usage: 27.3 MB, less than 74.19% of Python online submissions for Prefix and Suffix Search.'''