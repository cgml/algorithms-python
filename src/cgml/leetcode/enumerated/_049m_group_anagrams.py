from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for w in strs: d[''.join(sorted(w))].append(w)
        return [v for k, v in d.items()]