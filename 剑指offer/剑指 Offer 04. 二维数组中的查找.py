'''
3 分钟前	通过
'''


class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        i = 0
        j = n - 1
        while i < m and j >= 0:
            # print("i= ",i, " j=", j)
            if matrix[i][j] < target:

                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False