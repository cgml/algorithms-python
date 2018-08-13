class Solution:
    def validPalindrome(self, s, l=None,r=None, maxdeletes=1):
        if l is None: l, r = 0, len(s)-1
        while l<r:
            while l<r and not s[l].isalnum(): l+=1
            while l<r and not s[r].isalnum(): r-=1
            if l<r and s[l].lower()!=s[r].lower():
                if maxdeletes > 0: return self.validPalindrome(s,l+1,r,maxdeletes-1) or self.validPalindrome(s,l,r-1,maxdeletes-1)
                else: return False
            l,r = l+1,r-1
        return True


assert not Solution().validPalindrome("abc")
assert Solution().validPalindrome("cabc")
assert not Solution().validPalindrome("ccabc")
assert Solution().validPalindrome("ccabcc")