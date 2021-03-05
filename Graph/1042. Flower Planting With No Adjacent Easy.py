'''
https://leetcode.com/problems/flower-planting-with-no-adjacent/submissions/
'''

class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        Graph = {}
        for i in range(N):
            Graph[i] = []
        visited = [0] * N
        for i, j in paths:
            Graph[ i -1].append( j -1)
            Graph[ j -1].append( i -1)

        for i in range(N):
            visited[i] = ({1, 2, 3, 4} - {visited[j] for j in Graph[i]}).pop()
        return visited


'''
Success
Details 
Runtime: 400 ms, faster than 88.49% of Python online submissions for Flower Planting With No Adjacent.
Memory Usage: 20.1 MB, less than 100.00% of Python online submissions for Flower Planting With No Adjacent.
'''
