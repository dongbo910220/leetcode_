'''
https://leetcode.com/problems/friend-circles/
'''


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        rows = len(M)
        cols = len(M[0])

        visited = [0] * rows
        count = 0

        for i in range(rows):
            if visited[i] == 0:
                visited[i] = 1
                self.dfs(M, i, visited)
                count += 1
        return count

    def dfs(self, M, person, visited):
        for other in range(len(M)):
            if M[person][other] == 1 and visited[other] == 0:
                visited[other] = 1
                self.dfs(M, other, visited)

'''
Success
Details 
Runtime: 164 ms, faster than 93.18% of Python online submissions for Friend Circles.
Memory Usage: 13.1 MB, less than 11.11% of Python online submissions for Friend Circles.
'''
