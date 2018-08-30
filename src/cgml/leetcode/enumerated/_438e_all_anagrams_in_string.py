class Solution(object):
    def findAnagrams(self, s, p):
        K = len(p)
        ds, dp = {}, {}
        for item in p: dp[item]=dp.get(item,0)+1
        result = []
        for idx, item in enumerate(list(s)):
            if idx >= K and s[idx - K] in ds:
                popchar = s[idx - K]
                ds[popchar]=ds.get(popchar,0)-1
                if ds[popchar]<=0: del ds[popchar]
            ds[item]=ds.get(item,0)+1
            if len(ds) == len(dp) and ds == dp: result.append(idx-K+1)
        return result


from collections import Counter

class SolutionCounter:
    def findAnagrams(self, s, p):
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            sCounter[s[i]] += 1  # include a new char in the window
            if len(sCounter) == len(pCounter) and sCounter == pCounter:  # This step is O(1), since there are at most 26 English letters
                res.append(i - len(p) + 1)  # append the starting index
            sCounter[s[i - len(p) + 1]] -= 1  # decrease the count of oldest char in the window
            if sCounter[s[i - len(p) + 1]] == 0:
                del sCounter[s[i - len(p) + 1]]  # remove the count if it is 0
        return res

print(Solution().findAnagrams("abab", "ab"))
print(Solution().findAnagrams("ababa", "aba"))
