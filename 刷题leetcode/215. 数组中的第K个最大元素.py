'''
执行结果：
通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了96.46% 的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了69.79% 的用户
'''

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()     #一会儿验证下
        # print(nums)
        nums1 = nums[::-1]
        return nums1[k-1]


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = len(nums) - k
        num_k = self.helper(nums, 0, len(nums) - 1, i)
        return num_k

    def helper(self, nums, l, r, i):
        pos = self.partion(nums, l, r)
        if pos == i:
            return nums[pos]
        elif pos > i:
            return self.helper(nums, l, pos - 1, i)
        else:
            return self.helper(nums, pos + 1, r, i)

    def partion(self, nums, l, r):
        # choose the left ele to be the pivot
        pivot = nums[l]

        while l < r:
            while l < r and nums[r] > pivot:
                r -= 1
            if l < r:
                nums[l] = nums[r]
                l += 1
            while l < r and nums[l] < pivot:
                l += 1
            if l < r:
                nums[r] = nums[l]
                r -= 1
        nums[l] = pivot
        return l