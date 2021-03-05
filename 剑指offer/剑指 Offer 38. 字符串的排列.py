'''

执行结果：
通过
显示详情
执行用时：92 ms, 在所有 Python 提交中击败了95.84% 的用户
内存消耗：20 MB, 在所有 Python 提交中击败了19.10% 的用户
'''


a = "1233asdf"
b = list(a)
print(b)
print(','.join(b))

class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]
                dfs(x + 1)
                c[i], c[x] = c[x], c[i]
        dfs(0)
        return res