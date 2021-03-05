'''
https://leetcode.com/problems/online-stock-span/
'''

class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res

'''
Success
Details 
Runtime: 452 ms, faster than 96.20% of Python online submissions for Online Stock Span.
Memory Usage: 17.8 MB, less than 32.98% of Python online submissions for Online Stock Span.
'''