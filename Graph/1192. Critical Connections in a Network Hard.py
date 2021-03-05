'''
https://leetcode.com/problems/critical-connections-in-a-network/
'''


class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = collections.defaultdict(list)
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)

        jump = [-1] * n

        def dfs(node, parent, level, res, jump):
            jump[node] = level

            for child in graph[node]:
                if child == parent:
                    continue
                elif jump[child] == -1:
                    jump[node] = min(jump[node], dfs(child, node, level + 1, res, jump))
                else:  # child has been used
                    jump[node] = min(jump[node], jump[child])

            if jump[node] == level and node != 0:
                res.append([node, parent])

            return jump[node]

        res = []
        dfs(0, -1, 0, res, jump)
        return res

'''
Success
Details 
Runtime: 2176 ms, faster than 81.38% of Python online submissions for Critical Connections in a Network.
Memory Usage: 87.3 MB, less than 100.00% of Python online submissions for Critical Connections in a Network.
'''