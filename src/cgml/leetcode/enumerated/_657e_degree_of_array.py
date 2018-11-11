from collections import Counter, defaultdict


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dc = Counter(nums)
        degree = max([v for k, v in dc.items()])
        keys = set([k for k, v in dc.items() if v == degree])
        f, d = {}, {}

        for idx, n in enumerate(nums):
            if n in keys:
                f[n] = f.get(n, idx)
                d[n] = idx - f[n] + 1

        return min([v for k, v in d.items()])
