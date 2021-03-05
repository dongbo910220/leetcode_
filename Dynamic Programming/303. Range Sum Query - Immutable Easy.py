'''
https://leetcode.com/problems/range-sum-query-immutable/
'''

'''
Success
Details 
Runtime: 996 ms, faster than 17.64% of Python online submissions for Range Sum Query - Immutable.
Memory Usage: 16.1 MB, less than 7.69% of Python online submissions for Range Sum Query - Immutable.
'''


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j + 1])


'''
Success
Details 
Runtime: 56 ms, faster than 99.82% of Python online submissions for Range Sum Query - Immutable.
Memory Usage: 16.5 MB, less than 7.69% of Python online submissions for Range Sum Query - Immutable.
'''

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.dp = [0] * n
        for i in range(len(nums)):
            if i == 0:
                self.dp[i] = nums[i]
            else:
                self.dp[i] = self.dp[i - 1] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i != 0:
            return self.dp[j] - self.dp[i - 1]
        else:
            return self.dp[j]
