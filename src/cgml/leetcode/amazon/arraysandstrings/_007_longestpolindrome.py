class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        leftmax, rightmax = 0, 0
        for idx in range(len(s)):
            def check_palindrome(left,right,leftmax,rightmax):
                while left>=0 and right<len(s) and s[left] == s[right]: left, right = left-1,right+1
                if right - left > rightmax - leftmax: return left+1, right
                else: return leftmax, rightmax
            leftmax, rightmax = check_palindrome(idx,idx, leftmax, rightmax)
            leftmax, rightmax = check_palindrome(idx,idx+1, leftmax, rightmax)
        return s[leftmax:rightmax]

print(Solution().longestPalindrome("babad"))