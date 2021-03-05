class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        # Output: 6
        # Explanation: [4, -1, 2, 1]  has the largest sum = 6.
        sum = -65535;
        for index, num in enumerate(nums):
            if num < sum:
                pass
            sum_maybe = num;
            sum_temp = num;
            for j in range(index+1, len(nums)):
                sum_temp = sum_temp + nums[j]
                if sum_temp > sum_maybe:
                    sum_maybe = sum_temp;
            if sum_maybe > sum:
                sum = sum_maybe
        return sum
#
a = Solution()
a_max = a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(a_max)
#
# a = [0] * 5
# print(a)



class Solution_DivideAndConquer(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        # Output: 6
        # Explanation: [4, -1, 2, 1]  has the largest sum = 6.
        A = nums
        if len(A) <= 1:
            return A[0]

        mid = len(A) // 2   #整数除法
        leftA =  A[:mid]
        rightA = A[mid:]

        leftMaxSum = self.maxSubArray(leftA)
        rightMaxSum = self.maxSubArray(rightA)

        maxLeftBorderSum = -float('Inf')
        leftBorderSum = 0
        for i in range(0, len(leftA))[::-1]:
            leftBorderSum = leftBorderSum + leftA[i]
            if leftBorderSum > maxLeftBorderSum:
                maxLeftBorderSum = leftBorderSum

        maxRightBorderSum = -float('Inf')
        rightBorderSum = 0
        for i in range(0, len(rightA)):
            rightBorderSum = rightBorderSum + rightA[i]
            if rightBorderSum > maxRightBorderSum:
                maxRightBorderSum = rightBorderSum

        crossMax = max(maxLeftBorderSum, maxRightBorderSum, maxLeftBorderSum+maxRightBorderSum)
        return max(crossMax, leftMaxSum, rightMaxSum)


# a = Solution_DivideAndConquer()
# a_max = a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# print(a_max)

class Solution_WorkOnline(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = nums
        maxSum = A[0]
        sum = A[0]
        for i in range(1, len(A)):
            sum =  max(A[i], sum + A[i])
            if sum > maxSum:
                maxSum = sum
        return maxSum

a = Solution_WorkOnline()
a_max = a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(a_max)
