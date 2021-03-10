class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        h = {}
        h[0] = 0
        h[1] = 1
        if n <= 1:
            return h[n]
        for i in range(2, n + 1):
            if i - 1 in h.keys():
                print("is here")
            h[i] = h[i - 1] + h[i - 2]

        return h[n]
