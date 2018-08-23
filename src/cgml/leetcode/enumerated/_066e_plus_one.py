class Solution(object):
    def plusOne(self, a):
        carry, idx = 1, len(a)-1
        while idx >= 0 and carry > 0: carry, a[idx], idx = (a[idx]+carry) // 10, (a[idx]+carry) % 10, idx-1
        if carry > 0: a.insert(0, carry)
        return a

assert Solution().plusOne([9,9,9]) == [1,0,0,0]