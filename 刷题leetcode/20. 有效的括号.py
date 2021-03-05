'''
执行结果：
通过
显示详情
执行用时：12 ms, 在所有 Python 提交中击败了97.57% 的用户
内存消耗：13 MB, 在所有 Python 提交中击败了70.17% 的用户
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, match =[], {')':'(',']': '[', '}': '{'}
        for ch in s:
            if ch in match:
                if not (stack and stack.pop() == match[ch]):
                    return False
            else:
                stack.append(ch)
        return not stack