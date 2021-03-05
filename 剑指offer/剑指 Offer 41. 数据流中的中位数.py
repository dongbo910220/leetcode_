'''
执行结果：
通过
显示详情
执行用时：568 ms, 在所有 Python 提交中击败了73.10% 的用户
内存消耗：25.2 MB, 在所有 Python 提交中击败了29.24% 的用户
'''
class MedianFinder(object):

    def __init__(self):
        """
        init
from heapq import heappop
from heapq import heappopialize your data structure here.
        """
        self.small_top = []
        self.big_top = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small_top) != len(self.big_top):
            heappush(self.small_top, num)
            heappush(self.big_top, -heappop(self.small_top))
        else:
            heappush(self.big_top, -num)
            heappush(self.small_top, -heappop(self.big_top))


    def findMedian(self):
        """
        :rtype: float
        """
        return self.small_top[0] if len(self.small_top) != len(self.big_top) else (self.small_top[0] - self.big_top[0]) / 2.0