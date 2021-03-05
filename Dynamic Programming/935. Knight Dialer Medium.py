'''
https://leetcode.com/problems/knight-dialer/
'''


class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        M = collections.defaultdict(int)

        moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

        total = 0
        for i in range(4):
            for j in range(3):
                total = (total + self.paths(M, i, j, N)) % MOD
        return total

    def paths(self, M, i, j, N):
        MOD = 10 ** 9 + 7
        # max = MOD
        if (i < 0 or j < 0 or i >= 4 or j >= 3 or (i == 3 and j != 1)):
            return 0
        if N == 1:
            return 1
        if M[(N, i, j)] > 0:
            return M[(N, i, j)]
        n = N
        M[(N, i, j)] = self.paths(M, i - 1, j - 2, n - 1) % MOD + self.paths(M, i - 2, j - 1, n - 1) % MOD + self.paths(
            M, i - 2, j + 1, n - 1) % MOD + self.paths(M, i - 1, j + 2, n - 1) % MOD + self.paths(M, i + 1, j + 2,
                                                                                                  n - 1) % MOD + self.paths(
            M, i + 2, j + 1, n - 1) % MOD + self.paths(M, i + 2, j - 1, n - 1) % MOD + self.paths(M, i + 1, j - 2,
                                                                                                  n - 1) % MOD
        return M[(N, i, j)]


class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        next = [[1] * 3 for _ in range(4)]
        next[3][0], next[3][2] = -1, -1

        ans = 0
        for time in range(N - 1):
            cur = next
            next = [[0] * 3 for _ in range(4)]
            next[3][0], next[3][2] = -1, -1
            for r, row in enumerate(cur):
                for c, val in enumerate(row):
                    if val < 0:
                        continue
                    for move_i, move_j in moves:
                        nr = r + move_i
                        nc = c + move_j
                        if 0 <= nr < 4 and 0 <= nc < 3 and next[nr][nc] != -1:
                            next[nr][nc] += val
                            next[nr][nc] %= MOD
        ans = sum(map(sum, next)) % MOD + 2
        return ans

'''
Success
Details 
Runtime: 4080 ms, faster than 13.84% of Python online submissions for Knight Dialer.
Memory Usage: 13 MB, less than 45.54% of Python online submissions for Knight Dialer.
'''