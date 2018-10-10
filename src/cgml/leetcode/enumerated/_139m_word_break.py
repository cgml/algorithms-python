class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        t = {}
        for w in wordDict:
            ct = t
            for idx, c in enumerate(w):
                ct[c] = ct.get(c, {})
                if idx == len(w) - 1: ct[c]['*'] = True
                ct = ct[c]
        mem = {}
        return self._helper(s, t, mem)

    def _helper(self, s, t, mem):
        if mem.get(s, None) is not None: return mem[s]
        ct, result = t, False
        for idx, c in enumerate(s):
            if c not in ct: break
            ct = ct[c]
            if ct.get('*', False):
                if idx == len(s) - 1 or self._helper(s[idx + 1:], t, mem):
                    result = True
                    break
        mem[s] = result
        return result