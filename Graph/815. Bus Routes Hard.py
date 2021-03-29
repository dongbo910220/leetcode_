'''
https://leetcode.com/problems/bus-routes/submissions/
'''


class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        to_routes = collections.defaultdict(set)
        for idx, route in enumerate(routes):
            for j in route:
                to_routes[j].add(idx)
        bfs = [(source, 0)]
        seen = set([source])
        for stop, bus in bfs:
            if stop == target:
                return bus
            for i in to_routes[stop]:
                for location in routes[i]:
                    if location not in seen:
                        bfs.append((location, bus+1))
                        seen.add(location)
                routes[i] = []
        return -1






'''
Success
Details 
Runtime: 404 ms, faster than 65.75% of Python online submissions for Bus Routes.
Memory Usage: 51.3 MB, less than 100.00% of Python online submissions for Bus Routes.

'''