'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals)):
            cur_start, cur_end = intervals[i]
            if res:
                head_, tail_ = res[-1]
                if head_ <= cur_start <= tail_:
                    hi = max(tail_, cur_end)
                    res[-1][1] = hi
                else:
                    res.append(intervals[i])
            else:
                res.append(intervals[i])
        return res
a = Solution()
a.merge([[1,3],[2,6],[8,10],[15,18]])


# class Solution(object):
#     def merge(self, intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         res = []
#         intervals.sort(key=lambda x: x[0])
#         for i in range(len(intervals)):
#             cur_head, cur_tail = intervals[i]
#             if res:
#                 head_, tail_ = res[-1]
#                 hi = min(cur_tail, tail_)
#                 lo = max(cur_head, head_)
#                 if hi >= lo:
#                     res[-1][1] = max(cur_tail, tail_)
#                 else:
#                     res.append(intervals[i])
#             else:
#                 res.append(intervals[i])
#
#         return res
