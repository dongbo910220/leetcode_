'''
https://leetcode.com/problems/redundant-connection/submissions/
'''

'''
Success
Details 
Runtime: 36 ms, faster than 96.27% of Python online submissions for Redundant Connection.
Memory Usage: 13 MB, less than 25.00% of Python online submissions for Redundant Connection.
'''


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        for i, j in edges:
            if i not in graph:
                graph[i] = []
            graph[i].append(j)
            if j not in graph:
                graph[j] = []
            graph[j].append(i)

        n = len(edges)
        parents = [i for i in range(n + 1)]

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra != rb:
                parents[rb] = ra
                return True
            else:  # ra = rb
                return False

        res = []
        for i, j in edges:
            if not union(i, j):
                res.append(i)
                res.append(j)
                return res
            else:
                continue