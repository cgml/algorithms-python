class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r, m = 0, x, x // 2
        while l < r:
            m = (l + r) // 2
            est = int(m ** 2)
            if est == x:
                break
            elif est > x:
                r = m - 1
            else:
                l = m + 1
#TODO CHECK        return r if abs(int(r ** 2) - x) < abs(int(l ** 2) - x) else l


print(Solution().mySqrt(123123123),11096)