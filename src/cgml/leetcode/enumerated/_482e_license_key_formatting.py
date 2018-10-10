class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S.replace('-','').upper()
        if not s: return s
        N, result = len(s), []
        if N % K > 0: result, s, N = [s[:N%K]], s[N%K:], N-N%K
        result += [s[idx:idx+K] for idx in range(N)[::K] if s[idx:idx+K]]
        return '-'.join(result)