'''
https://leetcode.com/problems/find-the-town-judge/
'''

'''
Success
Details 
Runtime: 648 ms, faster than 95.35% of Python online submissions for Find the Town Judge.
Memory Usage: 17.7 MB, less than 33.33% of Python online submissions for Find the Town Judge.
'''


class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        degree = [0] * N
        if N == 1:
            return 1

        Graph = {}
        for i in range(N):
            Graph[i] = []
        for i, j in trust:
            degree[j - 1] += 1
            Graph[i - 1].append(j - 1)
        max_num = 0
        max_idx = -1
        for i in range(N):
            if degree[i] > max_num:
                max_num = degree[i]
                max_idx = i
        if max_num == N - 1:
            if not Graph[max_idx]:
                return max_idx + 1
        return -1