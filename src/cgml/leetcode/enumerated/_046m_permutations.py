class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) == 1: return [[nums[0]]]
        for i in range(0, len(nums)):
            result += [[nums[i]] + l for l in self.permute(nums[:i] + nums[i + 1:])]
        return result


class SolutionUnique(object):
    def permute(self, nums):
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


print(Solution().permute([1,2,3]))
print(SolutionUnique().permute([1,2,3]))