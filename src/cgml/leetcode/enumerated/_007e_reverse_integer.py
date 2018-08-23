import math


class Solution(object):
    def reverse(self, x):
        result, sign, x = 0, -1 if x < 0 else 1, abs(x)
        while x != 0: result, x = result * 10 + x % 10, x // 10
        result *= sign
        return result if (result >= -2 ** 31) and result <= (2 ** 31 - 1) else 0


print(Solution().reverse(123))
print(Solution().reverse(1534236469))