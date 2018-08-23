class Solution(object):
    def rotate(self, a, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(a)
        k, sign = k % N, -1
        if k > N // 2: k, sign = (N-k), 1
        if N < 2 or k == 0: return
        if N % k == 0:
            for idx in range(k): self.rotatecycle(a,k,idx, sign)
        else: self.rotatecycle(a,k,0, sign)
        return a

    def rotatecycle(self, a, k, idx, sign):
        N, curidx, mem = len(a), idx, a[idx]
        while True:
            a[curidx] = a[(curidx + sign * k)%N]
            curidx = (curidx + sign * k)%N
            if idx == curidx: break
        a[(curidx - sign * k)%N]=mem

assert Solution().rotate([1,2,3,4,5,6], k = 4) == [3, 4, 5, 6, 1, 2]
assert Solution().rotate([1,2,3,4,5,6], k = 3) == [4, 5, 6, 1, 2, 3]
assert Solution().rotate([1,2,3,4,5,6,7], k = 3) == [5,6,7,1,2,3,4]