'''

Solution:
    move simultaniously from beginning and end of string towards center until:
        l >= r - return true
        l < r and alphanumerical characteras s[l] != s[r]
'''
class Solution:
    '''
    TC: O(n)
    SC: O(1)
    '''
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l<r:
            while l<r and not s[l].lower().isalnum(): l+=1
            while l<r and not s[r].lower().isalnum(): r-=1
            if l<r and s[l].lower() != s[r].lower(): return False
            l,r=l+1,r-1
        return True

import string
class SolutionConcise:
    '''
    TC: O(n)
    SC: O(n)
    '''
    def isPalindrome(self, s):
        s = s.translate(str.maketrans('', '', string.punctuation + ' ')).lower()
        return s == s[::-1]


assert Solution().isPalindrome("A man,a plan,a canal: Panama")
assert not Solution().isPalindrome("race a car")
assert SolutionConcise().isPalindrome("A man,a plan,a canal: Panama")
assert not SolutionConcise().isPalindrome("race a car")

