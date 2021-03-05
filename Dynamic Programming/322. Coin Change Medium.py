'''
https://leetcode.com/problems/coin-change/
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = amount + 1
        dp = [amount + 1] * n
        dp[0] = 0
        for i in range(1, n):
            minval = float('inf')
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]


'''
Success
Details 
Runtime: 1068 ms, faster than 60.56% of Python online submissions for Coin Change.
Memory Usage: 13.1 MB, less than 12.50% of Python online submissions for Coin Change.

'''