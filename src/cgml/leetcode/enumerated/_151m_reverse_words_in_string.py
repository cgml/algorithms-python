class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s
        s = ' '.join([w for w in s.strip().split(' ') if w]) #TODO!
        a, l, r = list(s), 0, len(s)-1
        while l<r: a[l], a[r], l, r = a[r], a[l], l+1, r-1
        l,r = 0, 1
        while l < r and r < len(a):
            while r < len(a) and a[r] != ' ': r+=1
            lidx, ridx = l, r-1
            while lidx < ridx: a[lidx], a[ridx], lidx, ridx = a[ridx], a[lidx], lidx+1, ridx-1
            l = r
            while l < len(a) and a[l] == ' ': l+=1
            r = l+1
        return ''.join(a)