'''
https://leetcode.com/problems/flood-fill/
'''

'''
Success
Details 
Runtime: 60 ms, faster than 82.78% of Python online submissions for Flood Fill.
Memory Usage: 12.7 MB, less than 9.09% of Python online submissions for Flood Fill.
'''

from collections import deque


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image:
            return image
        self.bfs(image, sr, sc, newColor)
        return image

    def bfs(self, image, sr, sc, newColor):
        sColor = image[sr][sc]
        if sColor != newColor:
            image[sr][sc] = newColor
            queue = deque([(sr, sc)])
            while queue:
                x, y = queue.popleft()
                for i, j in [x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]:
                    if 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == sColor:
                        image[i][j] = newColor
                        queue.append((i, j))
