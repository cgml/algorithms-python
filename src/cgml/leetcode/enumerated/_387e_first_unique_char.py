class Solution:
    def firstUniqChar(self, s):
        found = set()
        unique = set()
        for i in range(len(s)):
            if s[i] not in found:
                found.add(s[i])
                unique.add(s[i])
            else:
                if s[i] in unique: unique.remove(s[i])
        for i in range(len(s)):
            if s[i] in unique: return i
        return -1