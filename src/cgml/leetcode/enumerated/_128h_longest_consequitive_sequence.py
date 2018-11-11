class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_seq = 0
        nums = set(nums)  # takes care of duplicates and makes constant lookup
        for num in nums:
            # get to bottom of sequence
            if num - 1 not in nums:
                longest = 1
                cur = num
                while cur + 1 in nums:
                    longest += 1
                    cur += 1
                max_seq = max(max_seq, longest)

        return max_seq

class SolutionUnionFind:
    def longestConsecutive(self, nums):
        class Range:
            def __init__(self, l, u):
                self.l, self.u, self.root = l, u, None

        d = {}  # defaultdict(set)
        for n in nums:
            if n in d:
                continue
            elif n - 1 not in d and n + 1 not in d:
                d[n] = Range(n, n)  # .add(n)# = (n,n)
            elif n - 1 in d and n + 1 not in d:
                r = d[n] = d[n - 1]
                while r: r.u, r = max(n, r.u), r.root
            elif n + 1 in d and n - 1 not in d:
                r = d[n] = d[n + 1]
                d[n].l = n
                while r: r.l, r = min(n, r.l), r.root
            else:  # n+1 in d, n-1 in d, n not in d
                lr = d[n - 1]  # can be replaced with range - for true O(n) overall
                ur = d[n + 1]
                lr.root = ur
                lr.u = ur.u
                ur.l = lr.l
                d[n] = ur

        m_ = 0
        for k, r1 in d.items():
            p, r = r, r1
            while r.root: r.root.u, r.root.l, r, p = max(r.root.u, r.u), min(r.root.l, r.l), r.root, r
            m_ = max(p.u - p.l + 1, m_)
        return m_
