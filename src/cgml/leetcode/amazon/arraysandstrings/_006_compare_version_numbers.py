class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2, dv1, dv2 = version1.split("."), version2.split("."), 0, 0
        while v1 or v2:
            dv1, dv2 = dv1*10, dv2*10
            if v1: dv1+=int(v1.pop(0))
            if v2: dv2+=int(v2.pop(0))
        if dv1 > dv2: return 1
        elif dv1 < dv2: return -1
        else: return 0

assert Solution().compareVersion(version1 = "0.1", version2 = "1.1") == 1
assert Solution().compareVersion(version1 = "7.5.2.4", version2 = "7.5.3") == -1
assert Solution().compareVersion(version1 = "1.0.1", version2 = "1") == 1
