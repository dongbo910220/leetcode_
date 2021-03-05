'''
https://leetcode.com/problems/dice-roll-simulation/
'''


class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        kMod = 1000000007
        kMaxRolls = 15

        dp = [[[0] * (kMaxRolls + 1) for _ in range(6)] for _ in range(n + 1)]
        # print(dp)
        for i in range(6):
            dp[1][i][1] = 1

        for i in range(2, n + 1):
            for j in range(6):
                for last_j in range(6):
                    for k in range(1, rollMax[last_j] + 1):
                        if last_j != j:
                            dp[i][j][1] = (dp[i][j][1] + dp[i - 1][last_j][k]) % kMod
                        elif k < rollMax[last_j]:  # last_j == j
                            dp[i][j][k + 1] = dp[i - 1][last_j][k]

        # sum(map(sum,a))
        return sum(map(sum, dp[n])) % kMod

'''
Success
Details 
Runtime: 1404 ms, faster than 34.48% of Python online submissions for Dice Roll Simulation.
Memory Usage: 20.4 MB, less than 80.46% of Python online submissions for Dice Roll Simulation.'''