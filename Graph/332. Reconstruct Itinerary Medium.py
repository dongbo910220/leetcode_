'''
https://leetcode.com/problems/reconstruct-itinerary/
'''

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)

        for src in graph.keys():
            graph[src].sort(reverse=True)
        print(graph)

        stack = ["JFK"]
        res = []

        while stack:
            elem = stack[-1]
            if elem in graph and graph[elem]:
                stack.append(graph[elem].pop())
            else:
                res.append(stack.pop())
        return res[::-1]

'''
Success
Details 
Runtime: 76 ms, faster than 48.00% of Python online submissions for Reconstruct Itinerary.
Memory Usage: 12.9 MB, less than 7.69% of Python online submissions for Reconstruct Itinerary.
'''
