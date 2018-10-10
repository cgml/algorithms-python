import re
from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        wmax, c, banned = None, Counter(re.findall(r'[\w]+', paragraph.lower())), set(banned)
        for w in c:
            if w not in banned and (not wmax or c[w]>c[wmax]): wmax=w
        return wmax