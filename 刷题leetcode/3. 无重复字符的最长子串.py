'''
执行结果：
通过
显示详情
执行用时：52 ms, 在所有 Python 提交中击败了75.58% 的用户
内存消耗：14 MB, 在所有 Python 提交中击败了20.41% 的用户

Success
Details
Runtime: 52 ms, faster than 66.07% of Python online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.1 MB, less than 42.01% of Python online submissions for Longest Substring Without Repeating Characters.
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len
