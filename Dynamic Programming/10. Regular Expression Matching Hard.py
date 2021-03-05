'''
https://leetcode.com/problems/regular-expression-matching/
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

        for j in range(1, n2):
            pj = j - 1
            if p[pj] == "*":
                dp[0][j] = dp[0][j - 2]

        for j in range(1, n2):
            for i in range(1, n1):
                si = i - 1
                pj = j - 1
                if s[si] == p[pj] or p[pj] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[pj] == "*":
                    if dp[i][j - 2] == 1:
                        dp[i][j] = 1
                    elif s[si] == p[pj - 1] or p[pj - 1] == ".":
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = 0
                else:
                    dp[i][j] = 0

        return bool(dp[-1][-1])

'''
Success
Details 
Runtime: 48 ms, faster than 55.32% of Python online submissions for Regular Expression Matching.
Memory Usage: 12.7 MB, less than 6.38% of Python online submissions for Regular Expression Matching.
'''

