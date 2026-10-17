class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        result = []
        for i in range(n):
            seen = set()
            for j in range(i+1,n):
                third = -(nums[i] + nums[j])
                if third in seen:
                    triplet = [nums[i],nums[j],third]
                    triplet.sort()
                    if triplet not in result:
                        result.append(triplet)
                seen.add(nums[j])
        return result

        

        