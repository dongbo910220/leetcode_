'''
https://leetcode.com/problems/find-eventual-safe-states/
'''


class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        visited = [-1] * len(graph)
        res = []
        for i in range(len(visited)):
            if visited[i] == -1:
                self.dfs(i, visited, graph, res)
        res.sort()
        return res

    def dfs(self, i, visited, graph, res):
        visited[i] = 0
        for j in graph[i]:
            if visited[j] == 0:
                return False
            if visited[j] == -1 and not self.dfs(j, visited, graph, res):
                return False
        visited[i] = 1
        res.append(i)
        return True

'''
Success
Details 
Runtime: 596 ms, faster than 97.18% of Python online submissions for Find Eventual Safe States.
Memory Usage: 19.5 MB, less than 50.00% of Python online submissions for Find Eventual Safe States.
'''