'''
https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
'''

class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """

        class Solution(object):
            def numWays(self, steps, arrLen):
                """
                :type steps: int
                :type arrLen: int
                :rtype: int
                """
                maxpos = min(steps, arrLen)
                dp = [[0] * (maxpos + 1) for _ in range(steps + 1)]
                dp[1][0] = 1
                dp[1][1] = 1
                for i in range(2, steps + 1):
                    for j in range(maxpos):
                        if j == 0:
                            # dp[i][j] = ((dp[i-1][j] + dp[i-1][j+1]) % (10^9 + 7))
                            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j + 1]) % 1000000007
                        else:  # idx is in the middle
                            dp[i][j] = ((dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]) % (1000000007))
                            # dp[i][j] = (dp[i-1][j] + dp[i-1][j+1] + dp[i-1][j-1]) %1000000007
                        # if j > 0:
                        #     dp[i][j] = (dp[i-1][j] + dp[i-1][j+1] + dp[i-1][j-1]) %1000000007
                        # else:
                        #     dp[i][j] = (dp[i-1][j] + dp[i-1][j+1] ) %1000000007
                return dp[steps][0]