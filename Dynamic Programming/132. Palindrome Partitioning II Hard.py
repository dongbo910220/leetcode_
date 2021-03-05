'''
https://leetcode.com/problems/palindrome-partitioning-ii/
'''

# for i in range(4, 5):
#     print(i)
# print(range(1, 5))
# a=[1, 2, 3, 4, 5]
# print(a[0:1])

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0 or n == 1:
            return 0
        dp = [n] * n
        T = [[0] * n for i in range(n)]
        # print(T)
        for l in range(n):
            for i in range(0, n - l):
                j = i + l
                if l == 0:
                    T[i][j] = 0
                    continue
                if self.isPal(s[i:j + 1]):
                    T[i][j] = 0
                else:
                    T[i][j] = 1

        for i in range(n):
            if T[0][i] == 0:
                dp[i] = 0
            for j in range(0, i):
                if T[j + 1][i] == 0:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n - 1]

    def isPal(self, s):
        return s == s[::-1]


a = "abcbm"
print(Solution().minCut(a))