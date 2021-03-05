'''
执行结果：
通过
显示详情
执行用时：520 ms, 在所有 Python 提交中击败了10.81% 的用户
内存消耗：18.8 MB, 在所有 Python 提交中击败了50.67% 的用户
'''

class Solution(object):
    def smallestK(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        self.quickSort(arr, 0, len(arr) - 1)
        return arr[:k]

    def quickSort(self, arr, start, end):
        if start < end:
            pivot = arr[start]
            i, j = start, end
            while i < j:
                while i < j and arr[j] >= pivot:
                    j -= 1
                if i < j:
                    arr[i] = arr[j]
                    i += 1
                while i < j and arr[i] <= pivot:
                    i += 1
                if i < j:
                    arr[j] = arr[i]
                    j -= 1
            arr[i] = pivot
            self.quickSort(arr, start, i-1)
            self.quickSort(arr, i+1, end)