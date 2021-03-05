'''
https://leetcode.com/problems/number-of-operations-to-make-network-connected/submissions/
'''

'''
Success
Details 
Runtime: 592 ms, faster than 38.10% of Python online submissions for Number of Operations to Make Network Connected.
Memory Usage: 33.2 MB, less than 100.00% of Python online submissions for Number of Operations to Make Network Connected.
'''

class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        cables = len(connections)
        if cables < n - 1:
            return -1


        parents = [i for i in range(n)]

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return True
            else:
                parents[rb] = ra
                return False

        num = 0
        for i, j in connections:
            if union(i, j):
                num += 1

        need = -1
        for i in range(n):
            if parents[i] == i:
                need += 1

        if num > need:
            return need
        else:
            return num


