class Solution(object):
    def isValid(self, s):
        queue, match = [], {'(':')','{':'}','[':']'}
        for c in s:
            if match.get(c): queue.append(c)
            elif len(queue) == 0 or match.get(queue.pop()) != c: return False
        return len(queue) == 0



assert Solution().isValid("()")
assert Solution().isValid("()[]{}")
assert not Solution().isValid("(]")
assert not Solution().isValid("([)]")
assert Solution().isValid("{[]}")