'''
https://leetcode.com/problems/range-sum-query-mutable/submissions/
'''

'''
Success
Details
Runtime: 120 ms, faster than 91.94% of Python online submissions for Range Sum Query - Mutable.
Memory Usage: 16.7 MB, less than 25.00% of Python online submissions for Range Sum Query - Mutable.
'''


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.nums = nums
        self.BITree = [0] * (n + 1)
        self.init = True
        for i, num in enumerate(nums):
            self.update(i, num)
        self.init = False

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        if not self.init:
            val1 = val
            val = val - self.nums[i]
            self.nums[i] = val1
        i += 1
        while i < len(self.BITree):
            self.BITree[i] += val
            i += (i & -i)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        sumi = self.sumidx(i - 1)
        sumj = self.sumidx(j)
        return sumj - sumi

    def sumidx(self, i):
        total = 0
        i += 1
        while i:
            total += self.BITree[i]
            i -= (i & -i)
        return total