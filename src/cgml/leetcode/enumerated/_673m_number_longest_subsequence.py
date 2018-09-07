class Solution:
    def numberLS(self, nums):
        N = len(nums)
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

assert Solution().numberLS([1,3,5,4,7]) == 2
assert Solution().numberLS([1,3,5,4,7,10]) == 2
assert Solution().numberLS([2,2,2,2,2]) == 5
assert Solution().numberLS([3,2,2,2,2]) == 5