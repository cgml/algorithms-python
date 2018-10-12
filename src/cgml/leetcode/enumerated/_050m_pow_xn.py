class Solution:
    def myPow(self, x, n):
        def _pow(x, n):
            if x == 0: return 0 if n else 1
            if n == 0: return 1
            h = _pow(x, n // 2)
            return h * h if n % 2 == 0 else h * h * x

        return _pow(x, n) if n >= 0 else _pow(1.0 / x, -n)

class SolutionTX:
    def myPow(self, x, n):
        if n < 0: x, n = 1 / x, -n
        res = 1
        while n > 0:
            if n % 2 == 1: res *= x
            x, n = x*x, n >> 1
        return res
