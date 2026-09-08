class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        count = 0
        ans = 0
        for i in range(n):
            if nums[i] == 1:
                count+= 1
                if count>ans:
                    ans = count
            else:
                count = 0
        return ans



                    
        
        
        