'''
https://leetcode.com/problems/possible-bipartition/
'''

'''
Success
Details 
Runtime: 616 ms, faster than 100.00% of Python online submissions for Possible Bipartition.
Memory Usage: 18.7 MB, less than 100.00% of Python online submissions for Possible Bipartition.
'''

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = {}
        for i in range(1, N + 1):
            graph[i] = []
        for i, j in dislikes:
            graph[i].append(j)
            graph[j].append(i)

        n = N
        visited = [0] * (N + 1)
        ans = 1
        for i in range(1, n + 1):
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