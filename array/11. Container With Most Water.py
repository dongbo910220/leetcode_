'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for i , num1 in enumerate(height):
            for j in range(i+1, len(height)):
                the_height = height[j]
                area = (j - i) * min(height[i], height[j])
                if area > max_area:
                    max_area = area
        return max_area

class Solution_2(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i = 0
        j = len(height) -1
        while( i != j):
            area = (j - i) * min(height[i], height[j])
            if area > max_area:
                max_area = area
            if height[i] > height[j]:
                j = j - 1
            else:
                i = i + 1
        return max_area



# for i in range(len(b)-1, -1, -1):
#     print(i, b[i])

# a = Solution()
# print(a.maxArea([1,8,6,2,5,4,8,3,7]))
b = [1,8,6,2,5,4,8,3,7]
# for i in range(-1, -len(b)-1, -1):
#     print(i, b[i])
# for i in range(len(b)-1, -1, -1):
#     print(i, b[i])


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    n = len(height)
    j = n - 1
    i = 0
    maxarea = 0
    while i < j:
        width = j - i
        h = min(height[i], height[j])
        area = h * width
        if area > maxarea:
            maxarea = area
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
    return maxarea

print(maxArea([1,8,6,2,5,4,8,3,7]))