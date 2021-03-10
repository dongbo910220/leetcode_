'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for i in nums:
            result += [res + [i] for res in result]
        return result

a = Solution()
print(a.subsets([1,2,3]))

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def dfs(lst, nums, pos):
            result.append(lst[:])
            for i in range(pos, len(nums)):
                dfs(lst+[nums[i]], nums, i+1)


        dfs([], nums, 0)
        return result