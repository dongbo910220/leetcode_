'''
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
'''


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]

        while start < end:
            mid = (start + end) // 2
            # mid = start + (end - start) / 2
            smaller, larger = matrix[0][0], matrix[n - 1][n - 1]

            count, smaller, larger = self.count_less_equal(matrix, mid, smaller, larger)

            if count == k:
                return smaller
            if count < k:
                start = larger
            else:
                end = smaller

        return start

    def count_less_equal(self, matrix, mid, smaller, larger):
        count = 0
        n = len(matrix)
        row, col = n - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                larger = min(larger, matrix[row][col])
                row -= 1
            else:
                smaller = max(smaller, matrix[row][col])
                count += row + 1
                col += 1

        return count, smaller, larger

'''
Success
Details 
Runtime: 192 ms, faster than 66.77% of Python online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 18.2 MB, less than 53.55% of Python online submissions for Kth Smallest Element in a Sorted Matrix.
'''

from heapq import *


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        minHeap = []

        for i in range(min(k, len(matrix))):
            heappush(minHeap, (matrix[i][0], 0, matrix[i]))

        numberCount, number = 0, 0
        while minHeap:
            number, idx, row = heappop(minHeap)
            numberCount += 1
            if numberCount == k:
                break
            if len(row) > idx + 1:
                heappush(minHeap, (row[idx + 1], idx + 1, row))

        return number