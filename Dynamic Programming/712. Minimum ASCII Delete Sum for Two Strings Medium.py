'''
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
'''


class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        l1, l2 = len(s1), len(s2)
        dp = [[0] * (l2 + 1) for _ in range(l 1 +1)]
        for i in range(l1):
            for j in range(l2):
                if s1[i] == s2[j]:
                    dp[ i +1][ j +1] = dp[i][j] + ord(s1[i])
                else:
                    dp[ i +1][ j +1] = max(dp[i][ j +1], dp[ i +1][j])
        result = sum(map(ord, s 1 +s2)) - dp[l1][l2] * 2
        return result
