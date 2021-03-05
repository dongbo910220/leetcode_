'''
执行结果：
通过
显示详情
执行用时：36 ms, 在所有 Python 提交中击败了71.86% 的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了53.15% 的用户
'''


class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        startx = 0
        starty = 0
        _set = set()
        result = self.find(startx, starty, m, n, k, 0, _set)
        return result

    def find(self, i, j, m, n, k, count, _set):
        if i >= m or j >= n or i < 0 or j < 0 or self.digitSum(i, j) > k or (i, j) in _set:
            return 0
        _set.add((i, j))
        branch_count = self.find(i + 1, j, m, n, k, count, _set) + \
                       self.find(i, j + 1, m, n, k, count, _set)

        return branch_count + 1

    def digitSum(self, i, j):
        row = i // 10 + i % 10
        col = j // 10 + j % 10
        return row + col