'''
执行结果：
通过
显示详情
执行用时：120 ms, 在所有 Python 提交中击败了70.26% 的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了69.01% 的用户
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revertNum = 0
        while x > revertNum:
            revertNum = revertNum * 10 + x % 10
            x /= 10

        return x == revertNum or x == (revertNum // 10)