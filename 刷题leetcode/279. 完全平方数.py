class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n+1):
            j = 1
            while j ** 2 <= i:
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
                j += 1
        return dp[n]
#超时
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_nums = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1) ]
        def minNumSquares(k):
            if k in square_nums:
                return 1
            min_num = float('inf')

            for square in square_nums:
                if k < square:
                    break
                new_num = minNumSquares(k - square) + 1
                min_num = min(min_num, new_num)
            return min_num
        return minNumSquares(n)