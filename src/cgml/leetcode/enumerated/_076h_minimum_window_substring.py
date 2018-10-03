from collections import Counter


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == t: return s
        d, dt = {}, Counter(t)  # window content, target counts
        idxws, idx = 0, 0
        mws, mwe = -1, len(s)
        while idx < len(s):
            c = s[idx]
            if c in t:
                d[c] = d.get(c, 0) + 1
                while idxws < idx and (s[idxws] not in t or d.get(s[idxws], 0) > dt[s[idxws]]):
                    if s[idxws] in t:
                        d[s[idxws]] = d[s[idxws]] - 1
                    idxws += 1
                solution = True
                for cs in dt:
                    if dt[cs] > d.get(cs, 0):
                        solution = False
                        break
                if solution and (idx - idxws) < (mwe - mws): mws, mwe = idxws, idx
            idx += 1
        return "" if mwe == len(s) else s[mws:mwe + 1]
