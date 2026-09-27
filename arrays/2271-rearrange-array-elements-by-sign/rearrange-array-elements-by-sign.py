class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        ans = [0]*n
        pos = 0
        neg = 0
        for i in range(n):
            if nums[i] > 0:
                ans[2*pos] = nums[i]
                pos+=1
            else:
                ans[(2*neg)+1] = nums[i]
                neg+=1
        return ans
            



