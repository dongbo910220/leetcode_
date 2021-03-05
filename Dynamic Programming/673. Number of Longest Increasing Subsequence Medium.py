'''
https://leetcode.com/problems/number-of-longest-increasing-subsequence/

'''


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N <= 1: return N
        lengths = [0] * N
        counts = [1] * N

        for j, num in enumerate(nums):
            for i in xrange(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]
        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)

'''
Success
Details 
Runtime: 596 ms, faster than 93.83% of Python online submissions for Number of Longest Increasing Subsequence.
Memory Usage: 12.9 MB, less than 50.00% of Python online submissions for Number of Longest Increasing Subsequence.
'''