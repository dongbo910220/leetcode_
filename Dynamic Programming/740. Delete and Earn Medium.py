'''
https://leetcode.com/problems/delete-and-earn/
'''

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        points = [0] * 10001
        for num in nums:
            points[num] += num
        return self.rob(points)




    def rob(self, nums):
        prev = cur = 0
        for value in nums:
            prev, cur = cur, max(prev + value, cur)
        return cur