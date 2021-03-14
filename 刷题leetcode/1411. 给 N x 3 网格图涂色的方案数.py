'''
执行结果：
通过
显示详情
执行用时：68 ms, 在所有 Python 提交中击败了66.67% 的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了45.10% 的用户
'''

class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        f1 = 6
        f2 = 6
        for i in range(2, n + 1):
            f1, f2 = f1 * 2 + f2 * 2, f1 *2 + f2 * 3
        return (f1 + f2) % mod