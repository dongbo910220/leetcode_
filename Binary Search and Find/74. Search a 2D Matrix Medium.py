'''
https://leetcode.com/problems/search-a-2d-matrix/

Success
Details
Runtime: 48 ms, faster than 89.32% of Python online submissions for Search a 2D Matrix.
Memory Usage: 14.4 MB, less than 87.98% of Python online submissions for Search a 2D Matrix.
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])
        numLen = m * n
        left = 0
        right = numLen - 1

        def getval(idx):
            col = idx % n
            row = idx // n
            return matrix[row][col]

        while left <= right:
            mid = (left + right) // 2
            midval = getval(mid)
            if midval == target:
                return True
            elif midval < target:
                left = mid + 1
            else:
                right = mid - 1
        return False