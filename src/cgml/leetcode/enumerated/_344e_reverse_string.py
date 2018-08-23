class Solution:
    def reverseString(self, s):
        sout = [' '] * len(s)
        for idx in range(len(s)): sout[len(sout) - 1 - idx] = s[idx]
        return "".join(sout)

assert "abcdf" == Solution().reverseString(Solution().reverseString("abcdf"))