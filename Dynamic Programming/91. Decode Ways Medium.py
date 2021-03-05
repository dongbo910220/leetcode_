'''
https://leetcode.com/problems/decode-ways/
'''


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        dp = [0 for i in range(len(s) + 1)]

        dp[0] = 1
        if s[0] == "0":
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(2, len(s) + 1):
            if 0 < int(s[i - 1:i]) <= 9:  # s[i-1]
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]

'''
Success
Details
Runtime: 16 ms, faster than 93.44% of Python online submissions for Decode Ways.
Memory Usage: 12.9 MB, less than 8.70% of Python online submissions for Decode Ways.
'''