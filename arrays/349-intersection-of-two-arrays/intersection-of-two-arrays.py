class Solution(object):
    def intersection(self, nums1, nums2):
        set2 = set(nums2)
        result = []
        for num in set(nums1):
            if num in set2:
                result.append(num)
        return result

        
        