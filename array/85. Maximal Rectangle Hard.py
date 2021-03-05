'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
https://leetcode.com/problems/maximal-rectangle/
'''


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        MaxArea = 0
        heights = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if int(matrix[i][j]) == 0:
                    heights[j] = 0
                else:
                    heights[j] += int(matrix[i][j])
            ans = self.maxArea(heights)
            MaxArea = max(ans, MaxArea)
        return MaxArea

    def maxArea(self, heights):
        heights.append(0)
        ans = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                l = stack.pop()
                h = heights[l]
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                ans = max(h * w, ans)
            stack.append(i)
        heights.pop()
        return ans

a = Solution()
input = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
# print(a.maximalRectangle(input))

# b = Solution()
# print(b.maxArea([3, 1, 3, 2, 2]))


# a = dict([3, 1, 3, 2, 2])
# a.append([3, 1, 3, 2, 2])
print(1 != 2)