class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        for idx in range(len(s) - 1):
            if s[idx] == s[idx + 1] == '+':
                result.append(s[:idx] + '--' + s[idx + 2:])
        return result
