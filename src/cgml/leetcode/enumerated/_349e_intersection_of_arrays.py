class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #return list(set(nums1)-(set(nums1)-set(nums2)))
        #return list(set(nums1).intersection(nums2))
        return list(set(nums1) & set(nums2))

print(Solution().intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
print(Solution().intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))