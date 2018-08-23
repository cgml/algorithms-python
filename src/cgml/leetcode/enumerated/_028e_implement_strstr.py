class Solution:
    def strStr(self, text, pattern):
        if not text and not pattern or not pattern: return 0
        M, N, lps, j, result, i = len(pattern), len(text), [0] * len(pattern), 0, [], 0
        self.lps(pattern, M, lps)
        while i < N:
            if pattern[j] == text[i]: i, j = i+1, j+1
            if j == M: result, j = result+[i - j], lps[j-1]
            elif i < N and pattern[j] != text[i]:
                if j != 0: j = lps[j - 1]
                else: i += 1
        return result if result else [-1]

    def lps(self, pattern, M, lps):
        length, lps[0], i = 0, 0, 1
        while i < M:
            if pattern[i] == pattern[length]: length, lps[i], i = length+1, length+1, i+1
            else:
                if length != 0: length = lps[length - 1]
                else: lps[i], i = 0, i+1

assert Solution().strStr("abcdefbcdefdd","ef") == [4,9]