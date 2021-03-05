'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        final_pos = n - 1
        pos = 0
        return self.jumpEachStep(nums, pos, final_pos)

    def jumpEachStep(self, nums, pos, final_pos):
        if pos >= final_pos:
            return True
        if nums[pos] == 0:
            return False
        ans = False
        for footstep in range(nums[pos], 0, -1):
            ans1 = self.jumpEachStep(nums, pos + footstep, final_pos)
            if ans == 1:
                return True
            ans = ans or ans1
        return ans

# a = Solution()
# b = [3,2,1,0,4]
# c = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
# d = [1,2,2,6,3,6,1,8,9,4,7,6,5,6,8,2,6,1,3,6,6,6,3,2,4,9,4,5,9,8,2,2,1,6,1,6,2,2,6,1,8,6,8,3,2,8,5,8,0,1,4,8,7,9,0,3,9,4,8,0,2,2,5,5,8,6,3,1,0,2,4,9,8,4,4,2,3,2,2,5,5,9,3,2,8,5,8,9,1,6,2,5,9,9,3,9,7,6,0,7,8,7,8,8,3,5,0]
# print("solution1", a.canJump(d))
# for i, j in enumerate(b, -1):
#     print(i, j)


class Solution_1(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        final_pos = n - 1
        pos = 0
        lastPos = final_pos
        for i in range(final_pos - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        if lastPos == 0:
            return True
        else:
            return False


a = Solution_1()
b = [3,2,1,0,4]
c = [2,3,1,1,4]
# print("solution2", a.canJump(d))
# d = [[1,3],[2,6],[8,10],[15,18]]
#
# for i, term in enumerate(d):
#     c, d = term
#     print(c, d)
#     print(i)
a, b , c = 0, 0, 0
print(c)




