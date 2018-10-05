class Solution:
    def _search(self, nums, lidx, ridx, target):
        if target > nums[ridx] or target < nums[lidx]: return False
        while lidx < ridx and ridx < len(nums) and lidx >= 0:
            midx = (lidx + ridx) // 2
            if nums[lidx] == target or nums[ridx] == target or nums[midx] == target: return True
            elif nums[midx] < target: lidx = midx + 1
            else: ridx = midx - 1
        return False

    def _rotated_search(self, nums, lidx, ridx, target):
        if target in (nums[lidx], nums[ridx]): return True
        if ridx - lidx <= 1: return False
        if nums[ridx] > nums[lidx]: return self._search(nums, lidx, ridx, target)

        midx = (lidx + ridx) // 2
        if target == nums[midx]: return True
        if nums[lidx] < nums[midx]:
            if nums[lidx] < target < nums[midx]: return self._search(nums, lidx, midx, target)
            else: return self._rotated_search(nums, midx + 1, ridx, target)
        if nums[midx] < nums[ridx]:
            if nums[midx] < target < nums[ridx]: return self._search(nums, midx, ridx, target)
            else: return self._rotated_search(nums, lidx, midx - 1, target)
        return self._rotated_search(nums, lidx, midx - 1, target) or self._rotated_search(nums, midx + 1, ridx, target)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return False
        if len(nums) == 1: return nums[0] == target
        return self._rotated_search(nums, 0, len(nums) - 1, target)

print(Solution().search([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1],0))
print(Solution().search([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1],1))
print(Solution().search([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1],2))