class Solution:
    def reverseString(self, s):
        sout = [' ']*len(s)
        for idx in range(len(s)): sout[len(sout)-1-idx]=s[idx]
        return "".join(sout)

strings = ["","a","lasjf;askfd;alskfd","sdklsaedfe"]
solver = Solution()
for s in strings:
    assert solver.reverseString(solver.reverseString(s)) == s