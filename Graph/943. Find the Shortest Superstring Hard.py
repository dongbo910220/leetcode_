'''
https://leetcode.com/problems/find-the-shortest-superstring/
'''


class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """

        def getDistance(s1, s2):
            for i in range(len(s1)):
                if s2.startswith(s1[i:]):
                    return len(s1) - i
            return 0

        def pathToStr(A, G, path):
            res = A[path[0]]
            for i in range(1, len(path)):
                indices = G[path[i - 1]][path[i]]
                res += A[path[i]][indices:]
            return res

        n = len(A)
        G = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                G[i][j] = getDistance(A[i], A[j])
                G[j][i] = getDistance(A[j], A[i])

        dp = [[0] * n for _ in xrange(1 << n)]
        # (node, mask, path, repeat_len)
        Q = collections.deque([(i, 1 << i, [i], 0) for i in xrange(n)])
        l = -1
        P = []
        while Q:
            node, mask, path, dis = Q.popleft()
            if dis < dp[mask][node]:
                continue
            if mask == (1 << n) - 1 and dis > l:
                P, l = path, dis
                continue
            for i in range(n):
                next_mask = mask | (1 << i)
                if next_mask != mask and dp[mask][node] + G[node][i] >= dp[next_mask][i]:
                    dp[next_mask][i] = dp[mask][node] + G[node][i]
                    Q.append((i, next_mask, path + [i], dp[next_mask][i]))

        return pathToStr(A, G, P)

'''
Success
Details 
Runtime: 1520 ms, faster than 12.99% of Python online submissions for Find the Shortest Superstring.
Memory Usage: 26.5 MB, less than 100.00% of Python online submissions for Find the Shortest Superstring.'''




