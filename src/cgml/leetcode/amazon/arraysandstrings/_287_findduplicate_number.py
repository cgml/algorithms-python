class Solution:
    def findDuplicate(self, nums):
        slow, fast, finder = nums[0], nums[nums[0]], 0
        while slow != fast: slow, fast = nums[slow], nums[nums[fast]]
        while slow != finder: slow, finder = nums[slow], nums[finder]
        return slow


assert Solution().findDuplicate([4,3,2,1,2]) == 2