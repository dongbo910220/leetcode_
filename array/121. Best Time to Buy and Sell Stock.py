'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > sum:
                    sum = prices[j] - prices[i]
        return sum

# print(min([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit


