import math

import math

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets: pigs += 1
        return pigs

class SolutionOldSchool(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        return math.ceil(math.log2(buckets))-math.ceil(math.log2(minutesToTest / minutesToDie))
print(Solution().poorPigs(1000,15,60))