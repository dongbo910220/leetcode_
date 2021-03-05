'''
https://leetcode.com/problems/wildcard-matching/
'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        n1 = len(s) + 1
        n2 = len(p) + 1
        dp = [[0] * n2 for i in range(n1)]
        dp[0][0] = 1
        print(dp[0][0])

        for j in range(1, n2):
            pj = j - 1
            # 可以优化
            # if p[pj] == "?":
            #     dp[0][j] = dp[0][j-1]
            if p[pj] == "*":
                dp[0][j] = dp[0][j - 1]

        for j in range(1, n2):
            for i in range(1, n1):
                si = i - 1
                pj = j - 1
                if s[si] == p[pj] or p[pj] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[pj] == "*":
                    tmp = dp[i - 1][j] or dp[i][j - 1]
                    dp[i][j] = tmp
                else:
                    dp[i][j] = 0

        return bool(dp[-1][-1])

'''
Success
Details 
Runtime: 1016 ms, faster than 48.66% of Python online submissions for Wildcard Matching.
Memory Usage: 20.9 MB, less than 10.00% of Python online submissions for Wildcard Matching.
Next challenges:
'''