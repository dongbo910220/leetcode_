'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        total = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total += prices[i] - prices[i - 1]
        return total
'''
Success
Details 
Runtime: 44 ms, faster than 90.07% of Python online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 13.7 MB, less than 9.30% of Python online submissions for Best Time to Buy and Sell Stock II.
'''