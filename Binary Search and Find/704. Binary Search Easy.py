'''
https://leetcode.com/problems/binary-search/

Success
Details
Runtime: 224 ms, faster than 61.95% of Python online submissions for Binary Search.
Memory Usage: 13.7 MB, less than 64.34% of Python online submissions for Binary Search.
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums)
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid
            else:
                return mid
        return -1