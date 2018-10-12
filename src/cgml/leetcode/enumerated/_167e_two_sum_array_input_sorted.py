class Solution(object):
    def twoSum(self, numbers, t):
        if not numbers: return []
        def bs(nums, l, r, t):
            l, r = min(l, len(nums)-1), max(0, r)
            if nums[l] == t or l >= r: return l
            if nums[r] == t: return r
            midx = (l+r)//2
            if nums[midx] == t: return midx
            if nums[midx] > t: return bs(nums, l, midx-1, t)
            return bs(nums, midx+1, r, t)
        midx = bs(numbers, 0, len(numbers)-1, int(t/2))
        l, r, d = midx, midx+1, {}
        while l>=0 or r<len(numbers):
            if l >= 0:
                if numbers[l] in d: return list(sorted([d[numbers[l]]+1, l+1]))
                d[t-numbers[l]], l = l, l-1
            if r < len(numbers):
                if numbers[r] in d: return list(sorted([d[numbers[r]]+1, r+1]))
                d[t-numbers[r]], r = r, r+1
        return []