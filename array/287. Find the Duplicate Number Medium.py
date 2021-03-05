'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

'''
'''
Success
Details 
Runtime: 44 ms, faster than 96.69% of Python online submissions for Find the Duplicate Number.
Memory Usage: 14.5 MB, less than 7.14% of Python online submissions for Find the Duplicate Number.
'''
#Wrong!
# Demand O(1) extra space
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for i in range(len(nums)):
            if (h.get(nums[i], 0) == 0):
                h[nums[i]] = 1
            else:
                return nums[i]

#Right way!!!
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast, slow = nums[nums[0]], nums[0]
        while (fast != slow):
            fast = nums[nums[fast]]
            slow = nums[slow]
        fast = 0
        while (fast != slow):
            fast = nums[fast]
            slow = nums[slow]
        return fast








