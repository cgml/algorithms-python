class Solution:
    def longestPalindrome(self, s):
        result = ""
        for idx in range(0,len(s)):
            i=j=idx
            while i>=0 and j<len(s) and s[i] == s[j]:
                i-=1;j+=1
            s1=s[i+1:j]
            i=idx;j=idx+1
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1;j+=1
            s2=s[i+1:j]
            substr = s1 if len(s1)>len(s2) else s2
            if len(substr)>len(result): result = substr
        return result

assert Solution().longestPalindrome("babad") == "bab"
assert Solution().longestPalindrome("cbbd") == "bb"
