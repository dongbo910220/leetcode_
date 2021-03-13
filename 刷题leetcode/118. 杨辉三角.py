'''
执行结果：
通过
显示详情
执行用时：12 ms, 在所有 Python 提交中击败了91.17% 的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了71.37% 的用户
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = []
        last_cur = []
        for num in range(1, numRows+1):
            cur = []
            for i in range(num):
                if i == 0:
                    cur.append(1)
                elif i == num - 1:
                    cur.append(1)
                else:
                    val = last_cur[i] + last_cur[i-1]
                    cur.append(val)
            res.append(cur)
            last_cur = cur
        return res