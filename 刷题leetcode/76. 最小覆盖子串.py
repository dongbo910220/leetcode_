'''
https://leetcode-cn.com/problems/minimum-window-substring/solution/tong-su-qie-xiang-xi-de-miao-shu-hua-dong-chuang-k/
'''

from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = Counter(t)
        needCnt = len(t)
        res = (0, float('inf'))
        i = 0
        for j, c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:
                while True:
                    if need[s[i]] == 0:
                        break
                    need[s[i]] += 1
                    i += 1
                if j - i < res[1] - res[0]:
                    res = (i, j)
                need[s[i]] += 1
                i += 1
                needCnt += 1
        return '' if res[1] > len(s) else s[res[0]: res[1]+1]


from collections import Counter
class Solution2(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = Counter(t)
        needCnt = len(t) #record the amount of key
        i = 0
        res = (0, float('inf'))
        for j, c in enumerate(s):
            #slide right
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:
                while True:
                    #slide left
                    c_head = s[i]
                    if need[c_head] == 0:
                        break
                    need[c_head] += 1
                    i += 1
                # update
                if j - i < res[1] - res[0]:
                    res = (i, j)
                need[c_head] += 1
                i += 1
                needCnt += 1
        return '' if res[1] > len(s) else s[res[0]:res[1]+1]
a2=Solution2()
a2.minWindow("a", "aa")

from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = Counter()
        # check if counter default value is 0
        for char in t:
            need[char] += 1
        print(need)
        needCnt = len(t)
        i = 0
        res = (0, float('inf'))  # record the head idx and tail idx
        for j, c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:
                while True:
                    c_head = s[i]
                    if need[c_head] == 0:
                        break
                    need[c_head] += 1
                    i += 1
                if j - i < res[1] - res[0]:
                    res = (i, j)
                need[c_head] += 1
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]









