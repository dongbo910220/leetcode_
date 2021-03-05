'''
https://leetcode.com/problems/longest-common-subsequence/
'''

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                dp[i+1][j+1] = dp[i][j] + 1 if c1 == c2 else max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]

'''
Success
Details 
Runtime: 296 ms, faster than 93.56% of Python online submissions for Longest Common Subsequence.
Memory Usage: 20.4 MB, less than 78.47% of Python online submissions for Longest Common Subsequence.
'''