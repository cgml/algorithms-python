class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        product = [1]*length
        l, r = 0,length-1
        lprod = rprod = 1
        while l < length and r > -1:
            product[l] = product[l]*lprod
            product[r] = product[r]*rprod
            lprod = lprod * nums[l]
            rprod = rprod * nums[r]

            l += 1
            r -= 1
        return product

class SolutionOneLiner(object):
    def productExceptSelf(self, nums):
        product, l, r, lprod, rprod = [1]*len(nums), 0, len(nums)-1, 1, 1
        while l < len(nums) and r > -1:
            product[l], product[r], lprod, rprod, l, r = product[l]*lprod, product[r]*rprod, lprod * nums[l], rprod * nums[r], l+1, r-1
        return product


assert Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6]