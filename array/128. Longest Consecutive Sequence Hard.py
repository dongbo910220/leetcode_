'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h  = {}
        if len(nums) == 0:
            return 0
        # for num in nums:
        #     h[num] = 1
        for num in nums:
            if h.get(num, 0) != 0:
                continue
            elif h.get(num+1, 0) == 0 and h.get(num-1, 0) == 0:
                h[num] = 1
            elif h.get(num+1, 0) != 0 and h.get(num-1, 0) == 0:
                h[num] = h[num+1] +1
                h[num + h[num+1]] =  h[num+1] +1
            elif h.get(num-1, 0) != 0 and h.get(num+1, 0) == 0:
                h[num] = h[num-1] +1
                h[num - h[num-1]] =  h[num-1] +1
            else:  #h.get(num-1, 0) != 0 and h.get(num+1, 0) ！= 0:
                l = h[num-1]
                r = h[num+1]
                h[num - h[num-1]] = l + r + 1
                h[num + h[num+1]] = l + r + 1
                h[num] = 1
        return h[max(h, key=h.get)]

a = Solution()
# b = a.longestConsecutive([100, 4, 200, 1, 3, 2])
# c = a.longestConsecutive([0])
input = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]

c = a.longestConsecutive(input)
print(c)

# print(b)
# print(c)
