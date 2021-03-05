'''
https://leetcode.com/problems/dungeon-game/submissions/
'''

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m+1)]
        dp[m][n-1] = 1
        dp[m-1][n] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                minval = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                if minval <= 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = minval
        return dp[0][0]

'''
Success
Details 
Runtime: 56 ms, faster than 82.81% of Python online submissions for Dungeon Game.
Memory Usage: 13.5 MB, less than 25.00% of Python online submissions for Dungeon Game.
'''