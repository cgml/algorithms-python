class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        p1, p2 = time.split(':')
        """
        p1, p2 = time.split(':')
        digits = list(time.replace(':', ''))

        # . step 1
        px2 = self._helper(p2, '59', digits)
        if px2: return p1 + ':' + px2

        # . step 2
        px1 = self._helper(p1, '23', digits)
        if not px1: px1 = self._helper('00', p1, digits, False)

        # . step 3
        px2 = self._helper('00', p2, digits, False)
        return px1 + ':' + px2

    def _helper(self, lo, hi, digits, strict=True):
        import itertools
        for t in sorted(['{}{}'.format(p[0], p[1]) for p in itertools.product(digits, repeat=2)]):
            if strict and lo < t and t <= hi:
                return t
            elif not strict and lo <= t and t <= hi:
                return t
        return None