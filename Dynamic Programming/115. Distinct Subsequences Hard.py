'''
https://leetcode.com/problems/distinct-subsequences/
'''


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n1 = len(t)
        n2 = len(s)
        T = [[0] * (n2 + 1) for i in range(n1 + 1)]
        for j in range(n2 + 1):
            T[0][j] = 1

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s[j - 1] == t[i - 1]:
                    T[i][j] = T[i - 1][j - 1] + T[i][j - 1]
                else:
                    T[i][j] = T[i][j - 1]

        return T[n1][n2]
'''
Success
Details
Runtime: 116 ms, faster than 75.99% of Python online submissions for Distinct Subsequences.
Memory Usage: 16.9 MB, less than 22.22% of Python online submissions for Distinct Subsequences.
'''
for i in range(3, 0):
    print(i)