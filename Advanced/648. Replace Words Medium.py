'''
https://leetcode.com/problems/replace-words/

Success
Details
Runtime: 204 ms, faster than 58.88% of Python online submissions for Replace Words.
Memory Usage: 53.1 MB, less than 13.79% of Python online submissions for Replace Words.
'''


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True

    def find_prefix(self, word):
        node = self.root
        prefix = ''
        for letter in word:
            prefix += letter
            if letter not in node.children:
                return word
            else:
                if node.children[letter].word:
                    return prefix
                else:
                    node = node.children[letter]
        return word


class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for word in dict:
            trie.insert(word)

        words = []
        for word in sentence.split(' '):
            words.append(trie.find_prefix(word))
        return " ".join(words)