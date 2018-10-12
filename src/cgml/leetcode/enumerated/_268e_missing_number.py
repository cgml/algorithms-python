class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Hash set approach
        # s = set(nums)
        # for idx in range(0,len(nums)+1):
        #     if idx not in s: return idx

        # XOR approach
        # missing = len(nums)
        # for i, num in enumerate(nums): missing ^= i ^ num
        # return missing

        # Gauss approach
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)

