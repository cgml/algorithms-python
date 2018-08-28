class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = set()
        self._helper(nums,result)
        return [list(subs) for subs in result]+[[]]

    def _helper(self, nums, result):
        if not nums: return
        result.add(tuple(nums))
        for idx in range(len(nums)):
            candidate = tuple(nums[:idx]+nums[idx+1:])
            if candidate not in result: self._helper(list(candidate),result)


print(Solution().subsets([1,2,3,4,5,6,7,8,10,0]))