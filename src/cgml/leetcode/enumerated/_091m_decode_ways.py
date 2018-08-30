class Solution(object):
    def _helper(self, s, mem):
        if mem.get(s) is not None: return mem.get(s)
        if not s: return 1
        if int(s[0]) == 0: return 0
        result = self._helper(s[1:], mem)
        if len(s) > 1 and int(s[:2]) >= 1 and int(s[:2]) <= 26: result += self._helper(s[2:], mem)
        mem[s]=result
        return result

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem = {}
        return self._helper(s, mem)

print(Solution().numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"))