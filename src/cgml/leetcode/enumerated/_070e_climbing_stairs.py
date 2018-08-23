class Solution:
    def climbStairsTabular(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return n
        m, m[0], m[1] = [None] * (n + 1), 1, 1
        for idx in range(2, n + 1): m[idx] = m[idx - 1] + m[idx - 2]
        return m[n]

    def helper(self, n, mem):
        if n < 2: return 1
        if mem[n] is None: mem[n] = self.helper(n - 1, mem) + self.helper(n - 2, mem)
        return mem[n]

    def climbStairs(self, n):
        return self.helper(n, [None] * (n + 1))

assert Solution().climbStairsTabular(3)==3
assert Solution().climbStairs(3)==3