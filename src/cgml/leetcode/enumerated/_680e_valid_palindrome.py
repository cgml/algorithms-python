'''

TODO: Current implementation is O(N^2).
Can be solved in O(N), with sliding window and constant time of palindrome verification hash
'''
class Solution:
    def _checkAlphanumeric(self, c):
        return ord(c) >= ord('0') and ord(c) <= ord('9') or ord(c) >= ord('a') and ord(c) <= ord('z')

    def validPalindrome(self, s, l=None,r=None, deleted=False):
        if l is None: l = 0
        if r is None: r = len(s)-1
        while l<r:
            while l<r and not self._checkAlphanumeric(s[l]): l+=1
            while l<r and not self._checkAlphanumeric(s[r]): r-=1
            if l<r and s[l].lower()!=s[r].lower():
                if not deleted: return self.validPalindrome(s,l+1,r,deleted=True) or self.validPalindrome(s,l,r-1,deleted=True)
                else: return False
            l,r = l+1,r-1
        return True


assert Solution().validPalindrome("abca")
assert Solution().validPalindrome("aba")
assert not Solution().validPalindrome("abcd")