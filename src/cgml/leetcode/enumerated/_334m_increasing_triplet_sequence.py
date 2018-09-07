class Solution:
    def increasingTriplet(self, nums):
        one, pair = float('inf'), [float('inf'),float('inf')]
        for n in nums:
            if n > pair[-1]: return True
            if n > one: pair = [one,n]
            one = min(one,n)
        return False

class SolutionOriginal:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        if N < 3: return False
        pair = [nums[0],None]
        one = None
        for n in nums[1:]:
            if pair[1] is None:
                if pair[0] > n: pair[0] = n
                elif pair[0] < n: pair[1] = n
            elif pair[1] < n: return True
            elif n < pair[1]:
                if pair[0] < n: pair[1] = n
                elif n < pair[0]:
                    if one is None or n < one: one = n
                    elif one < n:
                        pair = [one,n]
                        one = None
        return False