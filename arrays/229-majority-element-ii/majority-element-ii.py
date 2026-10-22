class Solution(object):
    def majorityElement(self, nums):
        count = {}
        n = len(nums)
        ans = []
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num] = 1
        for num in count:
            if count[num]>n//3:
                ans.append(num)
        return ans


        