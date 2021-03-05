'''
https://leetcode.com/problems/network-delay-time/
'''

'''
超时
'''
import heapq
from collections import deque
from collections import defaultdict


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        distance = {node: float('inf') for node in range(1, N + 1)}
        self.dfs(graph, distance, K, 0)
        totalTime = max(distance.values())
        return totalTime if totalTime < float('inf') else -1

    def dfs(self, graph, distance, node, elapsedTimeSoFar):
        if elapsedTimeSoFar >= distance[node]:
            return
        distance[node] = elapsedTimeSoFar
        for neighbour, time in sorted(graph[node]):
            self.dfs(graph, distance, neighbour, elapsedTimeSoFar + time)

a = {}
a[1] = 2
a[5] = 10
print(a)
print(a.values())

import heapq
from collections import deque
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        elapsedTime, graph, queue = [0] + [float('inf')] * N, defaultdict(list), deque([(0, K)])
        for u, v, w in times:
            graph[u].append((v, w))
        while queue:
            time, node = queue.popleft()
            if time < elapsedTime[node]:
                elapsedTime[node] = time
                for v, w in graph[node]:
                    queue.append((time + w, v))
        mx = max(elapsedTime)
        return mx if mx < float('inf') else -1
'''
Success
Details 
Runtime: 484 ms, faster than 52.63% of Python online submissions for Network Delay Time.
Memory Usage: 15.5 MB, less than 7.14% of Python online submissions for Network Delay Time.
'''