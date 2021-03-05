'''
https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/


'''


class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

        def enough(x):
            return sum(min(x / i, n) for i in xrange(1, m + 1)) >= k

        l, r = 1, m * n
        while l < r:
            mid = (l + r) // 2
            if not enough(mid):
                l = mid + 1
            else:
                r = mid
        return l

'''
Success
Details 
Runtime: 660 ms, faster than 51.56% of Python online submissions for Kth Smallest Number in Multiplication Table.
Memory Usage: 12.7 MB, less than 77.78% of Python online submissions for Kth Smallest Number in Multiplication Table.
'''