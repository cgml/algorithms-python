class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counts = {}
        for cpd in cpdomains:
            cnt, domain = cpd.split(' ')
            d = domain.split('.')
            while d:
                dcur = '.'.join(d)
                counts[dcur] = counts.get(dcur, 0) + int(cnt)
                d.pop(0)
        return ['{} {}'.format(str(counts[k]), k) for k in counts]
