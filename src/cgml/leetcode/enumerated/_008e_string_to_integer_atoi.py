class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        if not s: return 0
        result, sign = 0, None
        for c in s:
            if sign is None and c == ' ': continue
            if sign is None and c in ['-', '+']:
                sign = -1 if c == '-' else 1
                continue
            if sign is None: sign = 1
            n = ord(c) - ord('0')
            if n < 0 or n > 9: break
            result = result * 10 + n

        return min(max(result * sign if sign else result, -2 ** 31), 2 ** 31 - 1)

print(Solution().myAtoi("   +0 123"))