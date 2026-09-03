class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        totalSum = sum(nums)
        expSum = n*(n+1)//2
        return expSum-totalSum
        