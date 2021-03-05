'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
'''
# Time Limit Exceeded
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final_pos = len(nums) - 1
        jumps = [len(nums)] * len(nums)
        jumps[final_pos] = 0
        for i in range(final_pos - 1, -1, -1):
            # print('i', i)
            for jump_ in range(0,nums[i] + 1):
                # print('jump_', jump_)
                if i + jump_ > final_pos:
                    break
                elif jump_ == 0:
                    continue
                elif jumps[i + jump_] < jumps[i] + 1:
                    # print('i', i, 'i + jump_', i + jump_)
                    if jumps[i + jump_] + 1 < jumps[i]:
                        jumps[i] = jumps[i + jump_] + 1
        # print(jumps)
        return jumps[0]

a = Solution()
print(a.jump([2,3,1,1,4]))

#Bingo
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final_pos = len(nums) - 1
        maxArea = 0
        currentMaxArea = 0
        res = 0
        for i in range(final_pos):
            maxArea = max(nums[i] + i, maxArea)
            if i == currentMaxArea:
                res += 1
                currentMaxArea = maxArea
        return res