'''
https://leetcode.com/problems/open-the-lock/

Success
Details
Runtime: 508 ms, faster than 88.80% of Python online submissions for Open the Lock.
Memory Usage: 13.9 MB, less than 71.27% of Python online submissions for Open the Lock.
'''


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadset = set(deadends)
        if '0000' in deadset:
            return -1

        seen = set(['0000'])
        queue = collections.deque()
        queue.append(('0000', 0))

        while queue:
            s, step = queue.popleft()
            if s == target:
                return step
            for i in range(len(s)):
                for j in [1, -1]:
                    change = chr(ord(s[i]) + j)
                    if change > '9': change = '0'
                    if change < '0': change = '9'
                    tmp = s[:i] + change + s[i + 1:]
                    if tmp not in deadset and tmp not in seen:
                        queue.append((tmp, step + 1))
                        seen.add(tmp)
        return -1
