class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a, result = [], 0
        while num > 0:
            a.append(0 if num & 1 == 1 else 1)
            num >>= 1
        ridx = len(a)-1
        while ridx >= 0 and a[ridx]==0: ridx-=1
        for idx in range(0,ridx+1)[::-1]: result = (result << 1) | a[idx]
        print(int(''.join([str(c) for c in a[::-1]]), 2))
        return result


print(Solution().findComplement(11))