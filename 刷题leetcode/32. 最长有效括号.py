class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        for i in range(len(s)):
            if s[i] == ")" and i - dp[i-1] - 1>= 0 and s[i - dp[i-1] - 1] == "(":
                dp[i] = dp[i-1] + 2
                if i - dp[i-1] - 2 >= 0:
                    dp[i] += dp[i - dp[i-1] - 2]
        return max(dp)