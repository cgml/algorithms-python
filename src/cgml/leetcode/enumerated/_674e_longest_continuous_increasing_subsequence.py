class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums: return 0
        if len(nums) < 2: return len(nums)
        result, sidx = 0, 0
        for idx in range(1,len(nums)):
            if nums[idx-1] >= nums[idx]: result, sidx = max(result, idx-sidx), idx
        result = max(result, len(nums)-sidx)
        return result

assert Solution().findLengthOfLCIS([2,2,2,2]) == 1
assert Solution().findLengthOfLCIS([1,2,2,2]) == 2
assert Solution().findLengthOfLCIS([1,2,12,2]) == 3
assert Solution().findLengthOfLCIS([]) == 0
