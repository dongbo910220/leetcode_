'''
https://leetcode.com/problems/word-ladder-ii/submissions/
'''


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        queue = [(beginWord, 1, [beginWord])]
        visited = {}
        wordListSet = set(wordList)
        found = False
        shortest_dist = -1
        res = []

        while queue:
            word, dist, path = queue.pop(0)
            if path == ["hit", "hot", "lot", "log"]:
                print(path)
            if found and dist > shortest_dist:
                break
            if word == endWord:
                found = True
                shortest_dist = dist
                res.append(path)
                continue
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = word[:i] + j + word[i + 1:]
                    # if tmp == 'lot':
                    #     print(tmp)
                    if (tmp not in visited or visited[tmp] == dist + 1) and tmp in wordListSet:
                        queue.append((tmp, dist + 1, path + [tmp]))
                        visited[tmp] = dist + 1

        return res