'''
https://leetcode.com/problems/longest-increasing-subsequence/
'''

'''
Success
Details 
Runtime: 988 ms, faster than 22.54% of Python online submissions for Longest Increasing Subsequence.
Memory Usage: 13 MB, less than 6.82% of Python online submissions for Longest Increasing Subsequence.
'''


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * n
        for i in range( n -2, -1, -1):
            for j in range( i +1, n):
                if nums[i] < nums[j]:
                    tmp = dp[j] + 1
                    dp[i] = max(tmp, dp[i])
        print(dp)
        return max(dp) + 1



class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tails = [0] * len(nums)
        size = 0
        for num in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1
                else:
                    j = m
            tails[i] = num
            size = max(i + 1, size)
        return size

'''
Success
Details 
Runtime: 48 ms, faster than 71.07% of Python online submissions for Longest Increasing Subsequence.
Memory Usage: 13.2 MB, less than 6.82% of Python online submissions for Longest Increasing Subsequence.
Next challenges:
'''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tails = [0] * len(nums)
        size = 0
        for num in nums:
            i, j = 0, size #  head and tail
            while i < j:
                mid = (i + j) // 2
                if tails[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            tails[i] = num
            if i + 1 > size:
                size += 1
        return size