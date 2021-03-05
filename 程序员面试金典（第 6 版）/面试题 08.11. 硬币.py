class Solution(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        coins = [25, 10, 5, 1]

        dp = [1] + [0] * n
        for coin in coins:
            for i in range(coin, n+1):
                dp[i] += dp[i-coin]
        print(dp)
        return dp[-1] % mod

a = Solution()
a.waysToChange(10)