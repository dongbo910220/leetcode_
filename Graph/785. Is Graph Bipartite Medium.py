'''
https://leetcode.com/problems/is-graph-bipartite/
'''
'''
Success
Details 
Runtime: 156 ms, faster than 82.93% of Python online submissions for Is Graph Bipartite?.
Memory Usage: 13 MB, less than 20.00% of Python online submissions for Is Graph Bipartite?.
'''

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        visited = [0] * n
        ans = 1
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                ans = ans and self.dfs(graph, visited, i)
        return ans

    def dfs(self, graph, visited, i):
        color = visited[i]
        ans = 1
        for other in graph[i]:
            if visited[other] == color:
                return False
            elif visited[other] == 0:
                if color == 1:
                    visited[other] = 2
                else:
                    visited[other] = 1
                ans = ans and self.dfs(graph, visited, other)
            else:
                continue
        return ans