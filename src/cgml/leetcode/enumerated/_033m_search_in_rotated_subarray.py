
class Solution:
    def search(self, nums, target):
        if not nums: return -1
        if len(nums) == 1: return 0 if nums[0] == target else -1

        l, midx, r = 0, 0, len(nums)-1
        while l <= r:
            midx = int((r-l)/2)+l
            if nums[midx] == target: return midx

            # case 1: target in first increasing part
            if nums[0] <= target:
                if nums[midx] < nums[0]: r = midx -1
                elif nums[midx] < target: l = midx+1
                else: r = midx-1
            # case 2: target in second increasing part
            else:
                if nums[midx] >= nums[0]: l = midx+1
                elif nums[midx] < target: l = midx + 1
                else: r = midx-1
        return -1



print(Solution().search([4, 5, 6, 7, 0, 1, 2],2))
print(Solution().search([3,1],1))

