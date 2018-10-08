from collections import Counter


class Solution(object):
    def numSpecialEquivGroups(self, A):
        if not A: return 0
        return len(set([self._convert(a) for a in A]))

    def _convert(self, s1):
        c1 = Counter(s1[::2])
        c2 = Counter(s1[1::2])
        c_ = ['{}{}'.format(c, c1[c]) for c in sorted(c1)] + ['{}{}'.format(c, c2[c]) for c in sorted(c2)]
        s = ','.join(c_)
        return s

