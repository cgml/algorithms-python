class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0 or len(nums[0]) == 0: return nums
        if len(nums) * len(nums[0]) != r * c: return nums
        ro, co, rn, cn, R, C, reshaped = 0, 0, 0, 0, len(nums), len(nums[0]), [[0 for _ in range(c)] for _ in range(r)]

        def next_rc(RN, CN, cr, cc):
            cc += 1
            if cc >= CN: cr, cc = cr + 1, 0
            if cr >= RN: cr, cc = -1, -1
            return (cr, cc)

        while ro >= 0:
            reshaped[rn][cn] = nums[ro][co]
            ro, co = next_rc(R, C, ro, co)
            rn, cn = next_rc(r, c, rn, cn)
        return reshaped