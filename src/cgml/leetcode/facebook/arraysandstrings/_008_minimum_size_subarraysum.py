class Solution(object):
    def minSubArrayLen(self, s, nums):
        if not nums or sum(nums) < s: return 0
        curmin, cstart, cur, csum = len(nums), 0, 0, 0
        while cur < len(nums):
            while cur < len(nums) and csum < s: csum, cur = csum+nums[cur], cur+1
            if cur <= len(nums):
                while cstart < cur and csum >= s: curmin, csum, cstart = min(curmin,cur-cstart), csum-nums[cstart], cstart+1
        return curmin

assert Solution().minSubArrayLen( s = 7, nums = [2,3,1,2,4,3]) == 2