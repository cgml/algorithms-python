class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        result = 0
        idx = 0
        while idx<len(s):
            if idx<len(s)-1 and d.get(s[idx:idx+2],0)>0:
                result += d.get(s[idx:idx+2],0) ; idx+=2
            else:
                result += d.get(s[idx],0) ; idx +=1
        return result

assert Solution().romanToInt('IV') == 4
assert Solution().romanToInt('III') == 3
assert Solution().romanToInt('LVIII') == 58