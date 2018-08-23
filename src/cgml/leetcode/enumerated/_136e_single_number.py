import functools

class Solution(object):
    def singleNumber(self, nums):
        return functools.reduce(lambda x, y: x ^ y, nums)

assert Solution().singleNumber([4,1,2,1,2]) == 4
assert Solution().singleNumber([1,2,1,2,3]) == 3
