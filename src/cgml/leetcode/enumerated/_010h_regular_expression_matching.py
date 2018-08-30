class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        DP = [[False]*(n+1) for i in range(m+1)]
        DP[0][0] = True
        for i in range(m+1):
            for j in range(1,n+1):
                if p[j-1] == '*':
                    DP[i][j] = DP[i][j-2] or (i > 0 and j > 1 and (p[j-2] == '.' or s[i-1] == p[j-2]) and DP[i-1][j])
                elif i > 0 and (p[j-1] == '.' or p[j-1] == s[i-1]):
                    DP[i][j] = DP[i-1][j-1]
        return DP[m][n]

class SolutionDFS(object):
    def _helper(self, s, p, mem):
        if not s and not p: return True
        if s and not p: return False
        if not mem.get("{}_{}".format(s,p), True): return False
        if p[0] == '*': return False  # incorrect input
        if len(p) == 1:
            if p[0] == '.':
                return True
            else:
                return p == s

        if p[0] == '.':
            if p[1] == '*':
                if len(p) == 2: return True # '.*' = matches anything
                if self._helper(s, p[2:], mem): return True
                for idx in range(1,len(s)):
                    if self._helper(s[idx:], p[2:], mem): return True
                    if self._helper(s[idx:], p, mem): return True
            else:
                if self._helper(s[1:], p[1:], mem): return True
        else:
            if p[1] == '*':
                if len(s) == 0: return True
                ids = 0
                if self._helper(s, p[2:], mem): return True
                while ids < len(s) and s[ids] == p[0]:
                    if self._helper(s[ids+1:], p[2:], mem): return True
                    if self._helper(s[ids+1:], p, mem): return True
                    ids += 1
                return len(p)==2 and ids == len(s)
            else:
                if s[0] == p[0] and self._helper(s[1:], p[1:], mem): return True

        mem["{}_{}".format(s,p)] = False
        return False

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        mem = {}
        return self._helper(s, p, mem)


class Solution3:
    cache = {}

    def isMatch(self, s, p):
        if (s, p) in self.cache: return self.cache[(s, p)]
        if not p: return not s
        if p[-1] == '*':
            if self.isMatch(s, p[:-2]):
                self.cache[(s, p)] = True
                return True
            if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch(s[:-1], p):
                self.cache[(s, p)] = True
                return True
        if s and (p[-1] == s[-1] or p[-1] == '.') and self.isMatch(s[:-1], p[:-1]):
            self.cache[(s, p)] = True
            return True
        self.cache[(s, p)] = False
        return False

print(Solution3().isMatch("aa",".*"))
print(Solution3().isMatch("aa","a*"))
print(Solution3().isMatch("ab",".*c"))
print(Solution3().isMatch("aab", "c*a*b"))
print(Solution3().isMatch("mississippi", "mis*is*p*."))
