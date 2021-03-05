'''
https://leetcode.com/problems/combination-sum-iii/
'''


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(k, n, 1, [], res)
        return res


    def dfs(self, k, n, index, path, res):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            res.append(path)
        for i in range(index, 10):
            self.dfs( k -1, n- i, i + 1, path + [i], res)

'''
Success
Details 
Runtime: 20 ms, faster than 69.75% of Python online submissions for Combination Sum III.
Memory Usage: 12.7 MB, less than 50.00% of Python online submissions for Combination Sum III.
'''