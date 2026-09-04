class Solution(object):
    def merge(self, nums1, m, nums2, n):
      union = []
      i,j = 0,0
      while i<m and j<n:
        if nums1[i]<nums2[j]:
            union.append(nums1[i])
            i+=1
        else:
            union.append(nums2[j])
            j+=1
      while i<m:
        union.append(nums1[i])
        i+=1
      while j<n:
        union.append(nums2[j])
        j+=1
      for k in range(m + n):
        nums1[k] = union[k]
        