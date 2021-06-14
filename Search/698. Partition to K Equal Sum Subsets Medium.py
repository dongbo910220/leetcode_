'''
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
'''

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sums = [0] * k
        subsum = sum(nums) / k
        nums.sort(reverse=True)
        l = len(nums)

        def walk(i):
            if i == l:
                return len(set(sums)) == 1
            for j in xrange(k):  # put num in every bucket
                sums[j] += nums[i]
                if sums[j] <= subsum and walk(i + 1):
                    return True
                sums[j] -= nums[i]
                if sums[j] == 0:
                    break
            return False

        return walk(0)

'''
Success
Details 
Runtime: 32 ms, faster than 78.61% of Python online submissions for Partition to K Equal Sum Subsets.
Memory Usage: 12.9 MB, less than 15.02% of Python online submissions for Partition to K Equal Sum Subsets.
'''

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sums = [0] * k
        total = sum(nums)
        if total % k != 0:
            return False
        subsum = val = total / k
        nums.sort(reverse=True)
        l = len(nums)

        def walk(i):
            if i == l:
                return True
            num = nums[i]
            for idx in xrange(k):
                sums[idx] += num
                if sums[idx] <= val and walk(i + 1):
                    return True
                sums[idx] -= num
                if sums[idx] == 0:
                    break
            return False
        # def walk(i):
        #     if i == l:
        #         return len(set(sums)) == 1
        #     for j in xrange(k):  # put num in every bucket
        #         sums[j] += nums[i]
        #         if sums[j] <= subsum and walk(i + 1):
        #             return True
        #         sums[j] -= nums[i]
        #         if sums[j] == 0:
        #             break
        #     return False

        return walk(0)
