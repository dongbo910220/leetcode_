'''
https://leetcode.com/problems/edit-distance/
'''


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        f = [[None for _ in range(n + 1)] for _ in range(m + 1)]
        # print(f)

        for i in range(m + 1):
            for j in range(n + 1):
                # initialization
                if i == 0:
                    f[i][j] = j
                    continue
                if j == 0:
                    f[i][j] = i
                    continue
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1

        return f[m][n]
'''
Success
Details 
Runtime: 232 ms, faster than 13.40% of Python online submissions for Edit Distance.
Memory Usage: 15.9 MB, less than 15.00% of Python online submissions for Edit Distance.
'''