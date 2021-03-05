'''
https://leetcode.com/problems/permutations-ii/
'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res, visited = [], [False] * len(nums)
        self.dfs(nums, visited, [], res)
        return res

    def dfs(self, nums, visited, path, res):
        if len(nums) == len(path):
            res.append(path)
            return
        for i in xrange(len(nums)):
            if not visited[i]:
                if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:
                    continue
                visited[i] = True
                self.dfs(nums, visited, path + [nums[i]], res)
                visited[i] = False


'''
Success
Details 
Runtime: 40 ms, faster than 88.60% of Python online submissions for Permutations II.
Memory Usage: 12.7 MB, less than 6.67% of Python online submissions for Permutations II.
'''
