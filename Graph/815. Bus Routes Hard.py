'''
https://leetcode.com/problems/bus-routes/submissions/
'''


from collections import deque
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        to_routes = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)
        # print(to_routes)
        bfs = [(S, 0)]
        seen = set([S])
        for stop, bus in bfs:
            if stop == T:
                return bus
                # pass
            for i in to_routes[stop]:  # select a route
                for j in routes[i]:
                    if j not in seen:
                        bfs.append((j, bus+1))
                        seen.add(j)
                routes[i] = []
        # print(seen)
        return -1







'''
Success
Details 
Runtime: 404 ms, faster than 65.75% of Python online submissions for Bus Routes.
Memory Usage: 51.3 MB, less than 100.00% of Python online submissions for Bus Routes.

'''