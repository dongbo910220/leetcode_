'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
执行结果：
通过
显示详情
执行用时：56 ms, 在所有 Python 提交中击败了29.84% 的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了41.78% 的用户

https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)

        totalLeft = (m + n + 1) // 2
        left = 0
        right = m
        while left < right:
            i = (left + right + 1) // 2
            j = totalLeft - i
            if nums1[i - 1] > nums2[j]:
                right =  i - 1
            else:
                left = i

        i = left
        j = totalLeft - i
        nums1left = nums1[i-1] if i != 0 else float('-inf')
        nums1right = nums1[i] if i != m else float('inf')
        nums2left = nums2[j-1] if j != 0  else float('-inf')
        nums2right = nums2[j] if j != n else float('inf')
        if (m + n) % 2 == 1:
            print("odd")
            return max(nums1left, nums2left)
        else:
            print("even")
            # print("left ",max(nums1left, nums2left))
            leftval = max(nums1left, nums2left)
            print("right ",min(nums1right, nums2right))
            rightval = min(nums1right, nums2right)
            return (leftval + rightval) / 2.0



class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A = nums1
        B = nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

a = Solution()
print(a.findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10], [11, 12]))