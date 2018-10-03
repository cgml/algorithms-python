'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int

        divident = N
        divisor = d
        N = d*2^pow1 + d*2^pow2+...d*2^powk+drem
        result = 2^pow1+...+2^powk
        pow{1-k} ~ {0:16}
        O(log^2N/d)
        """
        result, N, d, k, ps = 0, abs(dividend), abs(divisor), 0, 0
        positive = dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0
        while k >= 0:
            result += k
            if result >= 2147483648 and positive: result = 2147483647; break
            k, ps = self._helper(N, d)
            N -= ps

        result = result if positive else -result
        return result

    def _helper(self, N, d):
        if d > N: return -1, 0
        k, ps, cs = 0, 0, d
        while cs <= N:
            if k == 0:
                k = 1
            elif k == 1:
                k = 2
            else:
                k = k + k
            ps, cs = cs, cs + cs
        return k, ps