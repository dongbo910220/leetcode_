'''
https://leetcode.com/problems/filling-bookcase-shelves/

'''

class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        n = len(books)
        dp = [1000000] * (n+1)
        dp[0] = 0
        for j in range(1, n+1):
            tmp_width, i, h = 0, j, 0
            while i > 0:
                tmp_width += books[i-1][0]
                if tmp_width > shelf_width:
                    break
                h = max(h, books[i-1][1])
                dp[j] = min(dp[j], dp[i-1]+h)
                i -= 1
        return dp[-1]

'''
Success
Details 
Runtime: 40 ms, faster than 65.52% of Python online submissions for Filling Bookcase Shelves.
Memory Usage: 13.2 MB, less than 12.00% of Python online submissions for Filling Bookcase Shelves.
'''