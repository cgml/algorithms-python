from collections import Counter

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return sum([1 for k, v in Counter(s).items() if v % 2 == 1]) <= 1