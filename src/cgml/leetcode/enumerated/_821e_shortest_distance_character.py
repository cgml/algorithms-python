class Solution(object):
    def shortestToChar(self, S, C):
        result = [float('inf')]*len(S)
        for idx, s in enumerate(S):
            if s == C:
                l,r,cnt = idx, idx, 0
                while l>=0 and l != C: result[l], cnt, l = min(result[l],cnt), cnt+1, l-1
                cnt = 0
                while r < len(S) and r != C: result[r], cnt, r = min(result[r],cnt), cnt+1, r+1
        return result
print("loveleetcode")
print(Solution().shortestToChar(S = "loveleetcode", C = 'e'))