'''
https://leetcode.com/problems/find-peak-element/

Success
Details
Runtime: 28 ms, faster than 92.90% of Python online submissions for Find Peak Element.
Memory Usage: 12.8 MB, less than 65.92% of Python online submissions for Find Peak Element.
'''


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        n = right
        if len(nums) == 1:
            return 0

        while left <= right:
            mid = (left + right) // 2
            if mid == 0:
                if nums[mid] > nums[1]:
                    return 0
                else:
                    return 1
            if mid == n:
                if nums[mid] > nums[mid - 1]:
                    return mid
            else:  # mid != 0 or n
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    if nums[mid] < nums[mid - 1]:
                        right = mid - 1
                    elif nums[mid] < nums[mid + 1]:
                        left = mid + 1
