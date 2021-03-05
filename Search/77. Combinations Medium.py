'''
https://leetcode.com/problems/combinations/

Success
Details
Runtime: 612 ms, faster than 56.85% of Python online submissions for Combinations.
Memory Usage: 14.2 MB, less than 7.69% of Python online submissions for Combinations.
'''


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        n = n + 1

        def dfs(start, cur):
            if len(cur) == k:
                res.append(cur)
            for i in range(start, n):
                dfs(i + 1, cur + [i])

        dfs(1, [])
        return res