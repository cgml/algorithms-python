import collections as c
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open = "({["
        close = ")}]"
        dq = c.deque()
        for x in s:
            if x in open: dq.append(x)
            if x in close and (len(dq) == 0 or open.index(dq.pop()) != close.index(x)): return False
        return len(dq) == 0

assert Solution().isValid("()")
assert not Solution().isValid("())")
