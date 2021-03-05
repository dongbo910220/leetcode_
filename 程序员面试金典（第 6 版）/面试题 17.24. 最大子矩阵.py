matrix = [
   [-1,0],
   [0,-1]
]
tmp = matrix[0] + matrix[1]
# print(tmp)

# 执行结果：
# 通过
# 显示详情
# 执行用时：2324 ms, 在所有 Python 提交中击败了18.18% 的用户
# 内存消耗：14.4 MB, 在所有 Python 提交中击败了27.27% 的用户
class Solution(object):
    def getMaxMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        self.maxval = -float('inf')

        m, n = len(matrix), len(matrix[0])
        r1, c1, r2, c2 = -1, -1, -1, -1
        for i in range(m):
            tmp = [0] * n
            for j in range(i, m):
                # 处理每一行
                maxval = 0
                for l in range(n):
                    tmp[l] += matrix[j][l]
                    if l == 0:
                        tmp1 = 0
                        maxval = tmp[0]
                    else:
                        if maxval + tmp[l] > tmp[l]:
                            maxval = maxval + tmp[l]
                        else:
                            maxval = tmp[l]
                            tmp1 = l
                    if maxval > self.maxval:
                        self.maxval = maxval
                        r1 = i
                        r2 = j
                        c1 = tmp1
                        c2 = l

        return [r1, c1, r2, c2]

    # def findmaxline(self, tmp, n):
    #     dp = [0] * n
    #     maxval = 0
    #     c1 = -1
    #     c2 = -1
    #     retval = False
    #     for i, num in enumerate(tmp):
    #         if i == 0:
    #             dp[i] = num
    #             c1 = 0
    #             c2 = 0
    #             maxval += num
    #         else:
    #             if dp[i-1] + num > num:
    #                 dp[i] = dp[i-1] + num
    #             else:
    #                 dp[i] = num
    #                 c1 = i
    #         if dp[i] > self.maxval:
    #             self.maxval = dp[i]
    #             self.startcol = c1
    #             self.endcol = i
    #             retval = True
    #             # print(tmp)
    #     return retval

    # self.startLine = i
    # self.endLine = j


#超时
class Solution(object):
    def getMaxMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        self.maxval = -float('inf')

        m, n = len(matrix), len(matrix[0])
        self.startLine, self.endLine, self.startcol, self.endcol = -1, -1, -1, -1
        for i in range(m):
            for j in range(i, m):
                tmp = [0] * n
                # 处理每一行
                for l in range(n):
                    for k in range(i, j + 1):
                        tmp[l] += matrix[k][l]
                print(tmp, "i=", i, "j=", j)
                if self.findmaxline(tmp, n):
                    self.startLine = i
                    self.endLine = j
        return [self.startLine, self.startcol, self.endLine, self.endcol]

    def findmaxline(self, tmp, n):
        dp = [0] * n
        maxval = 0
        c1 = -1
        c2 = -1
        retval = False
        for i, num in enumerate(tmp):
            if i == 0:
                dp[i] = num
                c1 = 0
                c2 = 0
                maxval += num
            else:
                if dp[i - 1] + num > num:
                    dp[i] = dp[i - 1] + num
                else:
                    dp[i] = num
                    c1 = i
            if dp[i] > self.maxval:
                self.maxval = dp[i]
                self.startcol = c1
                self.endcol = i
                retval = True
                # print(tmp)
        return retval

        # self.startLine = i
        # self.endLine = j











