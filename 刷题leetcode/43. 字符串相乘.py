cclass Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                n1, n2 = (ord(num1[i])- ord("0")), (ord(num2[j])- ord("0"))
                tmp = n1 * n2 + res[i + j + 1]
                res[i + j + 1] = (tmp % 10)
                res[i+j] += (tmp // 10)

        for i, c in enumerate(res):
            if c != 0:
                return "".join(map(str, res[i:]))

        return "0"