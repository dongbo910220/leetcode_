'''
执行结果：
通过
显示详情
执行用时：32 ms, 在所有 Python 提交中击败了81.11% 的用户
内存消耗：20 MB, 在所有 Python 提交中击败了32.37% 的用户
'''

class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for num in nums:
            exist = h.get(num, -1)
            if exist == -1:
                h[num] = 1
            else:
                return num