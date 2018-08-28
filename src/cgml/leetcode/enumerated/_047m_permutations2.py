class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        self._helper(nums,[],result)
        return [list(r) for r in result]

    def _helper(self, nums, prefix, result):
        if not nums: result.add(tuple(prefix))
        N = len(nums)
        for idx in range(0,N):
            curprefix = prefix + [nums[idx]]
            candidate = tuple(curprefix + nums[:idx] + nums[idx + 1:])
            if candidate not in result:
                self._helper(nums[:idx] + nums[idx + 1:], curprefix, result)


print(Solution().permuteUnique([1,1,2]))
