'''
https://leetcode-cn.com/problems/power-set-lcci/

解法简洁：https://leetcode-cn.com/problems/power-set-lcci/solution/jie-jin-shuang-100jie-ti-zhao-dao-di-tui-gong-shi-/
'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[],]
        if not nums:
            return res

        for num in nums:
            res += [[num]+ arr for arr in res]
        return res