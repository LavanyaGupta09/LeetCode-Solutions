class Solution(object):
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]
        n = len(nums)
        for i in range(n):
            for j in range(n-1-i):
                 if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
                     nums[j],nums[j+1] = nums[j+1],nums[j]
        if nums[0] == "0":
            return "0"
        return "".join(nums)
        nums = [3,30,34,5,9]
        print(largestNumber(nums))
        
        """
        :type nums: List[int]
        :rtype: str
        """
        