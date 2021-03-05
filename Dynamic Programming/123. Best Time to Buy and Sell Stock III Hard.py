'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

发现一个非常好的讲解
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * n for _ in range(3)]
        for k in range(1, 3):
            min_val = prices[0]
            for i in range(1, n):
                min_val = min(min_val, prices[i] - dp[k - 1][i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - min_val)

        return dp[2][n - 1]

'''
Success
Details 
Runtime: 60 ms, faster than 77.33% of Python online submissions for Best Time to Buy and Sell Stock III.
Memory Usage: 14.4 MB, less than 9.09% of Python online submissions for Best Time to Buy and Sell Stock III.
'''