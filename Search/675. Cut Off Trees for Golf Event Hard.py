'''
https://leetcode.com/problems/cut-off-trees-for-golf-event/
'''


class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        G = forest
        if not G and not G[0]: return -1
        m, n = len(G), len(G[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if G[i][j] > 0:
                    trees.append((G[i][j], i, j))
        trees = sorted(trees)
        count = 0
        cx, cy = 0, 0
        for h, x, y in trees:
            step = self.bfs(G, cx, cy, x, y)
            if step == -1:
                return -1
            else:
                count += step
                cx, cy = x, y
                G[x][y] = 1
        return count

    def bfs(self, G, cx, cy, x, y):
        visited = [[False for j in range(len(G[0]))] for i in range(len(G))]
        visited[cx][cy] = True
        queue = collections.deque()
        queue.append((cx, cy, 0))
        while queue:
            i, j, step = queue.popleft()
            if i == x and j == y:
                return step
            for ni, nj in [i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]:
                if 0 <= ni < len(G) and 0 <= nj < len(G[0]) and G[ni][nj] != 0 and not visited[ni][nj]:
                    queue.append((ni, nj, step + 1))
                    visited[ni][nj] = True
        return -1

'''
Success
Details 
Runtime: 7516 ms, faster than 34.59% of Python online submissions for Cut Off Trees for Golf Event.
Memory Usage: 12.9 MB, less than 96.60% of Python online submissions for Cut Off Trees for Golf Event.
'''