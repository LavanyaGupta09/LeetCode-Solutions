class Solution:
    def singleNumber(self, nums):
        xorr = 0
        for num in nums:
            xorr = xorr ^ num
        return xorr    