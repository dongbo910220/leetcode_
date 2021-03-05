'''
https://leetcode.com/problems/delete-operation-for-two-strings/
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
        dp = [[None for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j ==0 :
                    dp[i][j] = 0
                    continue
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return m + n - 2 * (dp[-1][-1])

'''
Success
Details 
Runtime: 332 ms, faster than 30.99% of Python online submissions for Delete Operation for Two Strings.
Memory Usage: 14.6 MB, less than 70.77% of Python online submissions for Delete Operation for Two Strings.
'''