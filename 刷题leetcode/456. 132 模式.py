class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        numsi = nums[0]
        for j in range(1, n-1):
            for k in range(j+1, n):
                if numsi < nums[k] and nums[j] > nums[k]:
                    return True
            numsi = min(nums[j], numsi)
        return False

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        n = len(nums)
        leftmin = [float('inf')] * n
        leftmin[0] = nums[0]
        for i in range(1, n):
            leftmin[i] = min(leftmin[i-1], nums[i])
        for i in range(n-1, -1 ,-1):
            num = nums[i]
            numk = -float('inf')
            while stack and stack[-1] < num:
                numj = num
                numk = stack.pop()
            if numk > leftmin[i]:
                return True
            stack.append(num)
        return False