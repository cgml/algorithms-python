import collections as c

class Solution:
    def twoSumIdx(self, nums, target):
        result = []
        pairs = {}
        for idx, num in enumerate(nums):
            if pairs.get(num) is not None: result += [[v, idx] for v in pairs.get(num)]
            if pairs.get(target-num) is None: pairs[target-num]=[]
            pairs.get(target-num).append(idx)
        return result

    def twoSum(self, nums, target):
        result = []
        pairs = {}
        for idx, num in enumerate(nums):
            if pairs.get(num) is not None: result += [[v, num] for v in pairs.get(num)]
            if pairs.get(target-num) is None: pairs[target-num]=[]
            pairs.get(target-num).append(num)
        return result

    def fourSum(self, nums, target):
        result = set()
        for idx in range(1,len(nums)-2):
            base = nums[idx]
            for idy in range(0,idx):
                for nv in [v + [base,nums[idy]] for v in self.twoSum(nums[idx+1:],target - base - nums[idy])]: nv.sort();result.add(tuple(nv))

        return [[v for v in x] for x in result]

assert Solution().fourSum([1, 0, -1, 0, -2, 2], 0) == [ [-1,  0, 0, 1], [-2,  0, 0, 2] , [-2, -1, 1, 2]]