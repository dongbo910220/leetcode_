'''
https://leetcode.com/problems/search-insert-position/

Success
Details
Runtime: 28 ms, faster than 98.84% of Python online submissions for Search Insert Position.
Memory Usage: 13.1 MB, less than 85.40% of Python online submissions for Search Insert Position.
'''


class Solution(object):
    def searchInsert(self, nums, target):
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
        return i