'''
https://leetcode.com/problems/combination-sum-ii/submissions/
'''

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        index = 0
        path = []
        res = []
        self.dfs(candidates, target, index, path, res)
        return res

    def dfs(self, candidates, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                pass
            else:
                self.dfs(candidates, target - candidates[i], i+1, path + [candidates[i]], res)


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []

        def combination_find(target, start, end, path):
            if target == 0:
                result.append(path)

            for i in range(start, end):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current = candidates[i]
                if current > target:
                    break

                remaining = target - current

                combination_find(remaining, i + 1, end, path + [current])

        combination_find(target, 0, len(candidates), [])
        return result

'''
Success
Details 
Runtime: 32 ms, faster than 92.31% of Python online submissions for Combination Sum II.
Memory Usage: 12.7 MB, less than 6.45% of Python online submissions for Combination Sum II.
'''