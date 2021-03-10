'''https://www.bilibili.com/video/BV1at411T75o?from=search&seid=751749115078251870'''
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.quickSort(nums)
        return nums

    #超时
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i -1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

    #超时
    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key

    def quickSort(self, nums):
        def helper(head, tail):
            if head >= tail: return
            l = head
            r = tail
            pivot = nums[head]
            while r > l:
                while nums[r] >= pivot and r > l:
                    r -= 1
                if r > l:
                    nums[l] = nums[r]
                    l += 1
                while nums[l] <= pivot and r > l:
                    l += 1
                if r > l:
                    nums[r] = nums[l]
                    r -= 1
            nums[l] = pivot
            helper(head, l-1)
            helper(l+1, tail)
        helper(0, len(nums)-1)
        return

a = [1,2,3,4,5]
b = a[:2]
c = a[2:]
print(id(a[0]),id(a[1]), id(b), id(c))