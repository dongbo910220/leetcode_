'''
执行结果：
通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了48.15% 的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了7.04% 的用户
'''

class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = ""
        l = len(s)
        i = 0
        idx = 0
        while i < l:
            if s[i] == ' ':
                s1 = s1+'%20'
            else:
                s1 = s1 + s[i]
            i += 1
        return s1
