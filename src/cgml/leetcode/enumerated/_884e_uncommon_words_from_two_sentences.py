from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        if not A and not B: return []
        return [k for k,v in (Counter(A.split(' '))+Counter(B.split(' '))).items() if v==1]