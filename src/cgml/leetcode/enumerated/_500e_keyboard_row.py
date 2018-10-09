class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result, d, kb = [], {}, ["qwertyuiop","asdfghjkl","zxcvbnm"]
        for idx, l in enumerate(kb):
            for c in l: d[c]=idx
        for w in words:
            if not w: continue
            idxs = [d[c] for c in w.lower()]
            if max(idxs) - min(idxs) == 0: result.append(w)
        return result