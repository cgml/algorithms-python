class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        if not S: return [0,0]
        lines, last_line = 1, 0
        for c in S:
            clen = widths[ord(c)-ord('a')]
            if last_line + clen > 100: lines, last_line = lines+1, clen
            else: last_line += clen
        return [lines, last_line]