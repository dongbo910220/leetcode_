'''
https://leetcode.com/problems/word-ladder/submissions/
'''
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList.append(beginWord)
        graph = collections.defaultdict(list)
        # initialization
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if self.isSimilar(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

        queue = collections.deque()
        queue.append((beginWord, 1))
        seen = set([beginWord])
        # print(graph)
        while queue:
            word, step = queue.popleft()
            # print(word)
            if word == endWord:
                return step
            for similarword in graph[word]:
                print(similarword)
                if similarword not in seen:
                    seen.add(similarword)
                    queue.append((similarword, step + 1))
        return 0

    def isSimilar(self, s1, s2):
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
        return diff == 1 or diff == 0


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue = [(beginWord, 1)]
        visited = set()
        wordListSet = set(wordList)

        while queue:
            word, dist = queue.pop(0)
            if word == endWord:
                return dist
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = word[:i] + j + word[i+1:]
                    if tmp not in visited and tmp in wordListSet:
                        queue.append((tmp, dist+1))
                        visited.add(tmp)
        return 0

