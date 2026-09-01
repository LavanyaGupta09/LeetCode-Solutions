class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        if n == 0:
            return
        k = k%n
        temp = nums[-k:]
        for i in range(n-k-1,-1,-1):
            nums[i+k] = nums[i]
        for i in range(k):
            nums[i] = temp[i]
sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
sol.rotate(nums, k)
print("Array after right rotation:", nums)