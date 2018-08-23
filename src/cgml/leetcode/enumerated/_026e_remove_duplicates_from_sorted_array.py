'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


'''
class Solution:
    def removeDuplicatesOnk(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        idx = 1
        while idx < len(nums):
            if nums[idx-1]==nums[idx]: nums.pop(idx)
            else: idx+=1
        return len(nums)

    def removeDuplicates(self, nums):
        if not nums: return 0
        cidx, ridx = 0, 1
        while ridx < len(nums):
            if nums[cidx]!=nums[ridx]: nums[cidx+1], cidx = nums[ridx], cidx+1
            ridx+=1
        return cidx+1

Solution().removeDuplicates([1,2])
assert Solution().removeDuplicates([r if r > 5 else 0 for r in range(20)])==15