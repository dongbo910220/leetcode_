'''
https://leetcode.com/problems/implement-magic-dictionary/
'''

class TrieNode(object):
    def __init__(self):
        self.word = False
        self.children = {}

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.word = True

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for word in dict:
            self.addWord(word)

    def findWord(self, remain, node, word):
        if not word:
            return True if remain == 0 and node.word else False
        for key in node.children.keys():
            if key == word[0]:
                if self.findWord(remain, node.children[key], word[1:]):
                    return True
            elif remain == 1:
                if self.findWord(0, node.children[key], word[1:]):
                    return True
        return False


    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return self.findWord(1, self.root, word)

'''
Success
Details 
Runtime: 32 ms, faster than 16.74% of Python online submissions for Implement Magic Dictionary.
Memory Usage: 12.8 MB, less than 57.66% of Python online submissions for Implement Magic Dictionary.
'''