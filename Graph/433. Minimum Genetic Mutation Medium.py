'''
https://leetcode.com/problems/minimum-genetic-mutation/submissions/

Success
Details
Runtime: 4 ms, faster than 100.00% of Python online submissions for Minimum Genetic Mutation.
Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Minimum Genetic Mutation.
'''

from collections import deque


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank.append(start)
        n = len(bank)
        end_idx = -1
        start_idx = n - 1
        graph = {}
        for i in range(n):
            graph[i] = []

        def similar(str1, str2):
            diff = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    diff += 1
            return diff == 1

        # print(bank[0], bank[1], similar(bank[0], bank[1]))

        for i in range(n):
            if bank[i] == end:
                end_idx = i
            for j in range(i + 1, n):
                if similar(bank[i], bank[j]):
                    graph[i].append(j)
                    graph[j].append(i)
        if end_idx == -1:
            return -1

        path = [float('inf')] * n
        path[n - 1] = 0

        queue = deque([n - 1])
        while queue:
            node = queue.popleft()
            for i in graph[node]:
                if path[node] + 1 < path[i]:
                    path[i] = path[node] + 1
                    queue.append(i)

        # print(path)
        # print(end_idx)
        # print(graph)
        if path[end_idx] < float('inf'):
            return path[end_idx]
        else:
            return -1
