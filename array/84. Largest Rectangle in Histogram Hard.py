'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.




Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].




The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10
https://leetcode.com/problems/largest-rectangle-in-histogram/
'''

#
# class Solution(object):
#     def largestRectangleArea(self, heights):
#         """
#         :type heights: List[int]
#         :rtype: int
#         """
#         heights.append(0)
#         stack = [0]
#         ans = 0
#         for i in range(1, len(heights)):
#             while stack and heights[i] < heights[stack[-1]]:
#                 h = heights[stack.pop()]
#                 if stack:
#                     w = i - stack[-1] - 1
#                 else:
#                     w = i
#                 ans = max(ans, h * w)
#             stack.append(i)
#         # heights.pop()
#         return ans



# use my own way
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)          #非常容易忘
        stack = []
        ans = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                ans = max(ans, h * w)
            stack.append(i)
        # heights.pop()
        return ans


a = Solution()
print(a.largestRectangleArea([3, 1, 3, 2, 2]))