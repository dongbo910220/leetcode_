class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = len(matrix)
        if row == 0 or len(matrix[0]) == 0:
            return []

        col = len(matrix[0])
        res = matrix[0]

        if row > 1:
            for i in range(1, row):
                res.append(matrix[i][col - 1])

            for j in range(col - 2, -1, -1):
                res.append(matrix[row - 1][j])

            if col > 1:  # should be considered
                for i in range(row - 2, 0, -1):
                    res.append(matrix[i][0])

        # update the matrix
        next_matrix = []
        for k in range(1, row - 1):
            new_row = matrix[k][1:-1]
            next_matrix.append(new_row)

        return res + self.spiralOrder(next_matrix)