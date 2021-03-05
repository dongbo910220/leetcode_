'''
https://leetcode.com/problems/time-based-key-value-store/

'''

a =  [ (1, 3),(1, 5)]
print(a[1][1])


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.dict[key].append([timestamp, value])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """

        arr = self.dict[key]
        n = len(arr)

        left = 0
        right = n

        while left < right:
            mid = (left + right) / 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid

        return "" if right == 0 else arr[right - 1][1]

'''
Success
Details 
Runtime: 728 ms, faster than 49.76% of Python online submissions for Time Based Key-Value Store.
Memory Usage: 71.2 MB, less than 10.03% of Python online submissions for Time Based Key-Value Store.
'''