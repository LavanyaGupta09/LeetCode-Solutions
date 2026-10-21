class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        pivot = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        if pivot != -1:
            for j in range(n-1,pivot,-1):
                if nums[j] > nums[pivot]:
                    nums[pivot],nums[j] = nums[j],nums[pivot]
                    break
        nums[pivot+1:] = reversed(nums[pivot+1:])
                