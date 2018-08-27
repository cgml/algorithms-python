class Solution(object):
    def trap(self, a):
        N = len(a)
        lmxs, rmxs = [0]*N, [0]*N
        rmxs[N-1], total = N-1, 0
        for idx in range(1, N):
            lmxs[idx]=idx if a[idx]>a[lmxs[idx-1]] else lmxs[idx-1]
        for idx in reversed(range(0, N-1)):
            rmxs[idx]=idx if a[idx]>a[rmxs[idx+1]] else rmxs[idx+1]
        for idx in range(N):
            total += max(min(a[lmxs[idx]], a[rmxs[idx]]) - a[idx], 0)
        return total

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))