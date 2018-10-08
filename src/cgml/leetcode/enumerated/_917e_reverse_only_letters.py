class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S: return S
        l, r, s = 0, len(S) - 1, list(S)
        while l < r:
            while l <= r and not self._letter(s[l]): l += 1
            while l <= r and not self._letter(s[r]): r -= 1
            if l < r: s[l], s[r], l, r = s[r], s[l], l + 1, r - 1
        return ''.join(s)

    def _letter(self, c):
        return ord(c.lower()) >= ord('a') and ord(c.lower()) <= ord('z')
print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"), "Qedo1ct-eeLg=ntse-T!")