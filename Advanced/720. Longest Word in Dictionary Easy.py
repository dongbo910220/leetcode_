'''
https://leetcode.com/problems/longest-word-in-dictionary/
'''


class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isword = False
        self.word = ''


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.isword = True
        node.word = word

    def bfs(self):
        queue = collections.deque([self.root])
        res = ''
        while queue:
            node = queue.popleft()
            for node2 in node.children.values():
                if node2.isword:
                    queue.append(node2)
                    if len(node2.word) > len(res) or (len(node2.word) == len(res) and node2.word < res):
                        res = node2.word
        return res


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.bfs()

'''
Success
Details 
Runtime: 140 ms, faster than 35.64% of Python online submissions for Longest Word in Dictionary.
Memory Usage: 15 MB, less than 5.19% of Python online submissions for Longest Word in Dictionary.'''