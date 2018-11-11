class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # if B in A: return 1
        # if B in A+A: return 2
        # if A not in B: return -1
        # c = B.split(A)
        # if len(c) == 1:
        #     return -1
        # elif max([len(s) for s in c]) == 0:
        #     return len(c) - 1
        # elif A.startswith(c[-1]) and A.endswith(c[0]) and (len(c) == 2 or max([len(s) for s in c[1:-1]]) == 0):
        #     return len(c) + 1
        # else:
        #     return -1
        m = ""
        for idx in range(int(len(B)/len(A)+2)):
            m+=A
            if B in m: return idx + 1
        return -1

print(Solution().repeatedStringMatch("bb", "bbbbbbb"))