class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        last_row = [0] * len(matrix[0])
        maxArea = 0
        for i in range(len(matrix)):
            new_row = [0] * len(matrix[0])
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    continue
                else:
                    new_row[j] = int(matrix[i][j]) + last_row[j]
            Area = self.computeArea(new_row)
            maxArea = max(maxArea, Area)
            last_row = new_row
        return maxArea

    def computeArea(self, heights):
        heights.append(0)
        stack = []
        area = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                area = max(w * h, area)
            stack.append(i)
        return area