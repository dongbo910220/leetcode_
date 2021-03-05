from collections import deque
from collections import defaultdict
# masks = [1 << i for i in range(5)]
# print(masks)
'''
https://leetcode.com/problems/shortest-path-visiting-all-nodes/
'''

from collections import deque


class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        queue = deque([(1 << x, x) for x in xrange(N)])
        dist = collections.defaultdict(lambda: N * N)
        for x in xrange(N): dist[1 << x, x] = 0

        all_visited = 2 ** N - 1
        while queue:
            cover, head = queue.popleft()
            d = dist[cover, head]
            if cover == all_visited:
                return d
            for child in graph[head]:
                cover2 = cover | (1 << child)
                if d + 1 < dist[cover2, child]:
                    dist[cover2, child] = d + 1
                    queue.append((cover2, child))

'''
Success
Details 
Runtime: 148 ms, faster than 33.01% of Python online submissions for Shortest Path Visiting All Nodes.
Memory Usage: 18.9 MB, less than 100.00% of Python online submissions for Shortest Path Visiting All Nodes.
'''


queue = deque((1 << x, x) for x in range(5))
queue2 = deque([(1 << x, x) for x in range(5)])
print(queue)
print(queue2)
dist = defaultdict(lambda: N*N)
dist[1] = 2
print(dist)

'''defaultdict(None, {(1, 0): 0, (2, 1): 0, (4, 2): 0, (8, 3): 0, (16, 4): 0})'''
# dist1 = defaultdict()
N = 5
dist1 = defaultdict(lambda: 50)
for x in range(5): dist1[1 << x, x] = 0
print(dist1[2])

