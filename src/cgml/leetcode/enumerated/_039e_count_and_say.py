class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return '1'
        s = [1]
        for n in range(1,n):
            ns, pidx, idx = [], 0, 1
            while idx < len(s):
                if s[pidx] != s[idx]:
                    ns+=[idx-pidx,s[pidx]]
                    pidx=idx
                idx+=1
            ns+=[idx-pidx, s[pidx]]
            s = ns
        return ''.join([str(v) for v in s])