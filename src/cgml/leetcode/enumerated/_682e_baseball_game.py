from collections import deque

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        lastvalid = deque([])
        sums = deque([])
        for op in ops:
            if op == 'C' and len(sums) > 0:
                lastvalid.pop()
                sums.pop()
            elif op == 'D':
                nv = lastvalid[-1]*2
                lastvalid.append(nv)
                if len(sums) > 0: nv += sums[-1]
                sums.append(nv)
            elif op == '+': # assume we have at least 2 previous valid values
                nv = lastvalid[-1]+lastvalid[-2]
                lastvalid.append(nv)
                if len(sums)>0: nv += sums[-1]
                sums.append(nv)
            else:
                nv = int(op)
                lastvalid.append(nv)
                if len(sums)>0: nv += sums[-1]
                sums.append(nv)
        return 0 if len(sums) == 0 else sums[-1]