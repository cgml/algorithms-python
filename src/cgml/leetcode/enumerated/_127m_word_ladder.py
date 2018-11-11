from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        d, v, q, cnt, w = defaultdict(list), set(), [beginWord], 0, None
        for w in wordList:
            for idx, c in enumerate(w): d[w[:idx]+'-'+w[idx+1:]].append(w)
        
        while q and w != endWord:
            L = len(q)
            for idx in range(L):
                w = q.pop(0)
                if w == endWord: break
                if w in v: continue
                v.add(w)
                for idx, c in enumerate(w):
                    for w2 in d[w[:idx]+'-'+w[idx+1:]]:
                        if w2 not in v: q.append(w2)
            cnt += 1
        return cnt if w == endWord else 0