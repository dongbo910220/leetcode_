'''
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
'''

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        d = [[float('inf')] * n for i in xrange(n)]
        for i, j, w in edges:
            d[i][j] = d[j][i] = w
        for i in xrange(n):
            d[i][i] = 0
        for k in xrange(n):
            for i in xrange(n):
                for j in xrange(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        res = {sum(dd <= distanceThreshold for dd in d[i]) : i for i in xrange(n)}
        # print(d)
        # print(res)
        return res[min(res)]

'''
Success
Details 
Runtime: 880 ms, faster than 23.16% of Python online submissions for Find the City With the Smallest Number of Neighbors at a Threshold Distance.
Memory Usage: 13.7 MB, less than 100.00% of Python online submissions for Find the City With the Smallest Number of Neighbors at a Threshold Distance.
'''


# res = {}
# res[2] = 5
# res[6] = 2
# res[8] = 5
# print(res[min(res)])
