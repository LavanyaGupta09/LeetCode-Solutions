class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[i]!=nums[j]:
                i+=1
                nums[i] = nums[j]
        return i+1
        