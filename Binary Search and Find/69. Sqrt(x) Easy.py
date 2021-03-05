'''
https://leetcode.com/problems/sqrtx/

Success
Details
Runtime: 20 ms, faster than 82.99% of Python online submissions for Sqrt(x).
Memory Usage: 12.7 MB, less than 40.37% of Python online submissions for Sqrt(x).
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 <= x < (mid+1)**2:
                return mid
            elif x < mid ** 2:
                right = mid
            else:
                left = mid + 1