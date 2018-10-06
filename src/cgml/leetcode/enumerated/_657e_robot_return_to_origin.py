from collections import Counter
class Solution(object):
    def judgeCircle(self, moves):
        c = Counter(moves)
        return c.get('U') == c.get('D') and c.get('L') == c.get('R')