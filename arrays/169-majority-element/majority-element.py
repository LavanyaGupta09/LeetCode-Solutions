class Solution(object):
    def majorityElement(self, nums):
      n = len(nums)
      count = {}
      for num in nums:
        if num in count:
            count[num] +=1
        else:
            count[num] = 1
        if count[num] > n//2:
             return num 