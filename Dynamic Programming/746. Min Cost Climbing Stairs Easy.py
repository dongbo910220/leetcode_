'''
https://leetcode.com/problems/min-cost-climbing-stairs/

Success
Details
Runtime: 68 ms, faster than 10.25% of Python online submissions for Min Cost Climbing Stairs.
Memory Usage: 12.8 MB, less than 52.52% of Python online submissions for Min Cost Climbing Stairs.
'''

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        spend = [0] * len(cost)
        spend[0] = cost[0]
        spend[1] = cost[1]
        for i in range(2, len(cost)):
            spend[i] = min(spend[i-2] + cost[i], spend[i-1] + cost[i])
        return min(spend[-1], spend[-2])