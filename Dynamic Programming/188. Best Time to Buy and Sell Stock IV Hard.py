'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
'''
'''
Success
Details 
Runtime: 64 ms, faster than 97.82% of Python online submissions for Best Time to Buy and Sell Stock IV.
Memory Usage: 13.3 MB, less than 12.50% of Python online submissions for Best Time to Buy and Sell Stock IV.
基本做出， 没考虑k过于大的情况
'''

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        if k >= (n / 2):
            return self.maxProfit2(prices)
        dp = [[0] * n for _ in range(3)]
        for kk in range(1, k + 1):
            kk = kk % 2
            if kk == 1:
                last_kk = 2
            else:
                kk = 2
                last_kk = 1
            min_val = prices[0]
            for i in range(1, n):
                min_val = min(min_val, prices[i] - dp[last_kk][i - 1])
                dp[kk][i] = max(dp[kk][i - 1], prices[i] - min_val)

        if k % 2 == 1:
            return dp[1][n - 1]
        else:
            return dp[2][n - 1]

    def maxProfit2(self, prices):
        total = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total += prices[i] - prices[i - 1]
        return total

