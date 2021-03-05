'''
https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/
'''

'''
Success
Details 
Runtime: 880 ms, faster than 5.41% of Python online submissions for Cheapest Flights Within K Stops.
Memory Usage: 13.8 MB, less than 26.32% of Python online submissions for Cheapest Flights Within K Stops.
'''

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = {}
        for i in range(n):
            graph[i] = {}
        for i, j, k in flights:
            graph[i][j] = k

        # visited = [float('inf')] * n
        # visited[src] = 0
        # maxcost = float('inf')
        def dfs(src, dst, K, cost):
            K = K - 1
            if K >= -1:
                for next_ in graph[src]:
                    if next_ == dst:
                        if cost + graph[src][next_] < self.maxcost:
                            self.maxcost = cost + graph[src][next_]
                            continue
                    # cost = cost + graph[src][next_]
                    if cost + graph[src][next_] > self.maxcost:
                        continue
                    dfs(next_, dst, K, cost + graph[src][next_])

        self.maxcost = float('inf')
        dfs(src, dst, K, 0)
        # print(visited)
        # print(graph)
        if self.maxcost == float('inf'):
            return -1
        else:
            return self.maxcost


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        f = collections.defaultdict(dict)
        for i, j, k in flights:
            f[i][j] = k
        heap = [(0, src, K+1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k-1))
        return -1


a = [(1, 5), (2, 3), (7, 1), (-1, 8)]
a.sort()
print(a)

'''
Success
Details 
Runtime: 132 ms, faster than 23.53% of Python online submissions for Cheapest Flights Within K Stops.
Memory Usage: 18.9 MB, less than 5.26% of Python online submissions for Cheapest Flights Within K Stops.
Next challenges:
'''
