class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        n, m, d = len(S), len(T), {}
        for i, s in enumerate(T): d.setdefault(s, []).append(i)
        dp, count, start = [-1]*m, n+1, -1

        for index, c in enumerate(S):
            if c in d:
                for i in d[c][::-1]:
                    if i == 0: dp[i] = index
                    else: dp[i] = dp[i - 1]
                    if i == m - 1 and dp[i] >= 0 and index - dp[i] + 1 < count:
                        count = index - dp[i] + 1
                        start = dp[i]
        return "" if dp[-1] < 0 else S[start:start + count]


print(Solution().minWindow(S = "abcdebdde", T = "bde"))
# class Solution(object):
#     def minWindow(self, S, T):
#         """
#         S = "abcdebdde", T = "bde"
#         :type S: str
#         :type T: str
#         :rtype: str
#         """
#         if not T: return ""
#         mem = {}
#         start, end = self.helper(S,T,mem)
#         return S[start:end+1] if start >= 0 else ""

#     def helper(self, s, t, mem, space=""):
#         if len(t)==0: return (0,0)
#         #mem[s]=mem.get(s,{})
#         if mem.get(s+" "+t) is not None: return mem.get(s+" "+t)
#         mem[s+" "+t] = (-1, float('inf'))
#         for idx in list(range(0,len(s)-len(t))):
#             if s[idx] == t[0]:
#                 v1min, v1max = self.helper(s[idx+1:],t[1:],mem, space+' ')
#                 v2min, v2max = self.helper(s[idx+1:],t,mem,space+' ')
#                 curmin, curmax = mem[s+ " "+t]
#                 if v1max-idx < curmax-curmin: curmin, curmax = idx, idx+v1max
#                 if v2max-v2min < curmax-curmin: curmin, curmax = idx+v2min, idx+v2max
#                 print("mem: {} {}, s[idx] = {}, curmin = {}, curmax {}".format(space+s, t, s[idx],curmin, curmax) )
#                 mem[s+" "+t]=(curmin,curmax)
#         #print(mem)
#         return mem[s+" "+t]


# class Solution(object):
#     def minWindow(self, S, T):
#         """
#         S = "abcdebdde", T = "bde"
#         :type S: str
#         :type T: str
#         :rtype: str
#         """
#         if not T: return ""
#         mem = {}
#         mstart, mend = -1, float('inf')
#         for idx, c in enumerate(S):
#             if c == T[0]:
#                 start, end = self.helper(S,0,T,mem,start=idx)
#         return S[start:end+1] if start >= 0 else ""

#     def helper(self, s, sidx, t, mem, start=None, initial=False):
#         if len(s)-sidx < len(t): return -1, float('inf')
#         if mem.get(t) is not None: return mem.get(t)
#         mem[t] = (-1, float('inf'))
#         idxs = list(range(sidx,len(s)-len(t)))
#         print(idxs)
#         for idx in idxs:
#             if s[idx] == t[0]:
#                 if len(t) == 1: hs, he = (start, idx+sidx)
#                 else: hs, he = self.helper(s, idx+1, t[1:], mem, start)
#                 if (he-start) < (mem[t][1]-mem[t][0]):
#                     # print('winner for char {}, sidx = {}, idx = {}, hs = {}, he = {}'.format(t[0],sidx,idx,hs, he))
#                     print('winner = mem[t] = {} / {} < {}. he={}, start={}, s[sidx:]={}, t={}'.format(mem[t],  (he-start), (mem[t][1]-mem[t][0]), he, start, s[sidx:],t))
#                     mem[t] = start, he

#         print(mem)
#         return mem[t]