'''
https://leetcode.com/problems/palindrome-partitioning-iii/

Accepted
'''


class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        N = len(s)
        cost = [[0] * N for _ in range(N)]
        for length in range(2, N + 1):
            for j in range(length - 1, N):
                i = j - length + 1
                cost[i][j] = (s[i] != s[j]) + cost[i + 1][j - 1]

        dp = [[10000] * (k + 1) for _ in range(N + 1)]
        for i in range(N):
            dp[i][1] = cost[0][i]
            for kk in range(2, k + 1):
                for j in range(0, i):
                    dp[i][kk] = min(dp[i][kk], dp[j][kk - 1] + cost[j + 1][i])
        return dp[N - 1][k]