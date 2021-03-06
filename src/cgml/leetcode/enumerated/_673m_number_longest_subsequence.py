class Solution:
    def findNumberOfLIS(self, nums):
        N = len(nums)
        if N <= 1: return N
        lengths = [0]*N
        counts = [1]*N
        for idx in range(N):
            for dpi in range(idx):
                if nums[dpi] < nums[idx]:
                    if lengths[dpi]+1 > lengths[idx]:
                        lengths[idx] = lengths[dpi]+1
                        counts[idx] = counts[dpi]
                    elif lengths[dpi]+1 == lengths[idx]:
                        counts[idx] += counts[dpi]
        maxlength = max(lengths)
        return sum([v for idx, v in enumerate(counts) if lengths[idx] == maxlength])

assert Solution().findNumberOfLIS([]) == 0
assert Solution().findNumberOfLIS([1]) == 1
assert Solution().findNumberOfLIS([1, 3, 5, 4, 7]) == 2
assert Solution().findNumberOfLIS([1, 3, 5, 4, 7, 10]) == 2
assert Solution().findNumberOfLIS([2, 2, 2, 2, 2]) == 5
assert Solution().findNumberOfLIS([3, 2, 2, 2, 2]) == 5