'''
执行结果：
通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了89.01% 的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了18.02% 的用户
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        #find i
        if i >= 0:
            # j start form tail
            j = len(nums) - 1
            while j > i and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1