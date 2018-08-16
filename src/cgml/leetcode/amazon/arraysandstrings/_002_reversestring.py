class Solution:
    def reverseString(self, s):
        return "".join(reversed(list(s)))

strings = ["","a","lasjf;askfd;alskfd","sdklsaedfe"]
solver = Solution()
for s in strings:
    assert solver.reverseString(solver.reverseString(s)) == s

