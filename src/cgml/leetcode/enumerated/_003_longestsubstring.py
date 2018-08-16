class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        curmax, cursubstr, sidx = 0, set(), 0
        for idx, c in enumerate(s):
            if c not in cursubstr:
                cursubstr.add(c)
            else:
                curmax = max(curmax, idx - sidx)
                while sidx < idx and s[sidx] != c:
                    cursubstr.remove(s[sidx])
                    sidx += 1
                if sidx < idx and s[sidx] == c: sidx += 1
        return max(curmax, len(cursubstr))
