'''
https://leetcode.com/problems/redundant-connection-ii/submissions/
'''

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        n = len(edges)
        candidates = [-1] * (n + 1)
        ans = -1
        ans1 = -1
        ans2 = -2
        wrong_node = -1
        state = True
        for idx, (i, j) in enumerate(edges):  # test
            if candidates[j] < 0:
                candidates[j] = i
            else:
                state = False
                wrong_node = j
                ans1 = candidates[j]
                ans2 = i
                ans = ans2
                edges[idx] = [-1, -1]

        for i, j in edges:
            if i >= 0:
                if i not in graph:
                    graph[i] = []
                graph[i].append(j)
                if j not in graph:
                    graph[j] = []
                graph[j].append(i)

        parents = [i for i in range(n + 1)]

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra != rb:
                parents[rb] = ra  # a parent
                return True
            else:  # ra = rb
                return False

        res = []
        for i, j in edges:
            if i >= 0:
                if not union(i, j):
                    if not state:
                        ans = ans1
                        break
                    else:
                        res.append(i)
                        res.append(j)
                        return res
                else:
                    continue

        res.append(ans)
        res.append(wrong_node)
        return res
















'''Success
Details
Runtime: 52 ms, faster than 35.42% of Python online submissions for Redundant Connection II.
Memory Usage: 13.2 MB, less than 100.00% of Python online submissions for Redundant Connection II.'''
