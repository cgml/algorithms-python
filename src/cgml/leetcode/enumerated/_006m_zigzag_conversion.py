class Solution:
    def convert(self, s, m):
        import math
        cs = 2*m-2 if m > 1 else 1
        chunks = int(math.ceil(len(s)/cs))
        result = []
        for r in range(m):
            for c in range(chunks):
                base = cs * c
                id1 = r
                if id1 + base < len(s):
                    result += s[id1+base]
                id2 = 2*m - r - 2
                if id2 >= m and id2 < 2*m - 2 and id2 + base < len(s):
                    result += s[id2+base]
        return "".join(result)

assert Solution().convert("PAYPALISHIRING",3) == "PAHNAPLSIIGYIR"
assert Solution().convert("AB",1) == "AB"