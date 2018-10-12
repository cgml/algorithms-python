class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Modified Boyer-Moore Majority Voting Algorithm
        c1, c2, cnt1, cnt2 = None, None, 0, 0
        for n in nums:
            if c1 == n:
                cnt1 += 1
            elif c2 == n:
                cnt2 += 1
            elif cnt1 == 0:
                c1, cnt1 = n, 1
            elif cnt2 == 0:
                c2, cnt2 = n, 1
            else:
                cnt1, cnt2 = cnt1 - 1, cnt2 - 1
        cnt1, cnt2 = 0, 0
        for n in nums: cnt1, cnt2 = (cnt1 + 1 if n == c1 else cnt1), (cnt2 + 1 if n == c2 else cnt2)
        return [v for v, cnt in [(c1, cnt1), (c2, cnt2)] if v is not None and cnt > len(nums) / 3]
