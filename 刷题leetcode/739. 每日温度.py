class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(T)
        stack = []

        for idx, v in enumerate(T):
            while stack and stack[-1][1] < v:
                index, value = stack.pop()
                ans[index] = idx - index
            stack.append([idx, v])
        return ans