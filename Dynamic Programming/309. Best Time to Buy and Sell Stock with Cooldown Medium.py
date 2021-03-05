'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices) + 1
        hold = [-float("inf")] * n
        sell = [0] * n
        rest = [0] * n
        i = 1
        for price in prices:
            hold[i] = max(hold[i-1], rest[i-1] - price)
            sell[i] = hold[i-1] + price
            rest[i] = max(sell[i-1], rest[i-1])
            i += 1
        return max(sell[n-1], rest[n-1])


a = [1, 3, 5, 7, 9]
a.insert(0, 0)
print(a)



'''
Success
Details 
Runtime: 28 ms, faster than 59.10% of Python online submissions for Best Time to Buy and Sell Stock with Cooldown.
Memory Usage: 12.8 MB, less than 7.69% of Python online submissions for Best Time to Buy and Sell Stock with Cooldown.
'''