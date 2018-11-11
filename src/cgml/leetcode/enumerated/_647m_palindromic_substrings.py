class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        res, i = 0, 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] == s[i]: j += 1
            res += (j - i) * (j - i + 1) // 2
            left, right = i - 1, j
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1
            i = j
        return res

# class Solution:
#     def countSubstrings(self, word):
#         all = 0
#         n = len(word)
#         start_end_paris = [(x,x) for x in range(n)] + [(x,x+1) for x in range(n-1)]
#         for (s,e) in start_end_paris:
#             while s>=0 and e<n and word[s]==word[e]:
#                 all+=1
#                 s-=1
#                 e+=1
#         return all