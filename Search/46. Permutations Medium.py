'''
https://leetcode.com/problems/permutations/
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res


    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[ i +1:], path + [nums[i]], res)

'''
Success
Details 
Runtime: 24 ms, faster than 89.06% of Python online submissions for Permutations.
Memory Usage: 12.7 MB, less than 6.00% of Python online submissions for Permutations.
'''