'''
https://leetcode.com/problems/stone-game-ii/

'''


class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        self.piles = piles
        self.n = len(piles)
        self.cache = [[0] * (2 * self.n + 1) for _ in xrange(self.n)]
        self.summary = [0] * self.n
        self.total = 0
        for i, pile in enumerate(piles):
            self.total = self.total + pile
            self.summary[i] = self.total
        return (self.total + self.solve(0, 1)) // 2

    def solve(self, s, M):
        if s >= self.n:
            return 0
        if self.cache[s][M] > 0:
            return self.cache[s][M]
        if s + 2 * M >= self.n:
            if s > 0:
                self.cache[s][M] = (self.total - self.summary[s - 1])
                return self.cache[s][M]
            else:
                self.cache[s][M] = self.total
                return self.cache[s][M]
        best = -float('inf')
        curr = 0
        for x in range(1, 2 * M + 1):
            curr += self.piles[s + x - 1]
            best = max(best, curr - self.solve(s + x, max(x, M)))
        self.cache[s][M] = best
        return self.cache[s][M]

a = [1,2,3,4,5]
print(sum(a[:3]))