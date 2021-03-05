'''
https://leetcode.com/problems/perfect-squares/
'''


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = float("inf")
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], (dp[i - j * j] + 1))
                j += 1
        return dp[n]

'''
Success
Details 
Runtime: 3964 ms, faster than 31.75% of Python online submissions for Perfect Squares.
Memory Usage: 13.1 MB, less than 24.00% of Python online submissions for Perfect Squares.
'''


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]
        q, nq, d = {n}, set(), 1
        while q:
            for node in q:
                for square in squares:
                    if node == square:
                        return d
                    elif node < square:
                        break
                    else:
                        nq.add(node - square)
            q, nq, d = nq, set(), d + 1

'''
Success
Details 
Runtime: 160 ms, faster than 90.94% of Python online submissions for Perfect Squares.
Memory Usage: 13.3 MB, less than 20.00% of Python online submissions for Perfect Squares.'''











