'''
https://leetcode.com/problems/shortest-path-with-alternating-colors/submissions/
'''

class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        G = [[[], []] for i in range(n)]
        for i, j in red_edges:
            G[i][0].append(j)
        for i, j in blue_edges:
            G[i][1].append(j)
        res = [[0, 0]] + [[float('inf'), float('inf')] for i in range(n - 1)]
        bfs = [[0, 0], [0, 1]]
        for i, color in bfs:
            for j in G[i][color]:
                if res[j][color] == float('inf'):
                    res[j][color] = res[i][1 - color] + 1
                    bfs.append([j, 1 - color])

        # res = [[3, 6], [5, 2]]
        # print(map(min, res))
        return [x if x < float('inf') else -1 for x in map(min, res)]

'''
Success
Details 
Runtime: 84 ms, faster than 34.48% of Python online submissions for Shortest Path with Alternating Colors.
Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Shortest Path with Alternating Colors.
'''


a = [1, 2]
print(a)
res = [[3, 6], [5, 2]]
a = [x for x in map(min, res)]
print(a)
print( map(min, res))