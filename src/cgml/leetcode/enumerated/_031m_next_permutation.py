class Solution(object):
    def quicksort(self, array, begin=0, end=None):
        def partition(array, begin, end):
            pivot = begin
            for i in range(begin + 1, end + 1):
                if array[i] <= array[begin]:
                    pivot += 1
                    array[i], array[pivot] = array[pivot], array[i]
            array[pivot], array[begin] = array[begin], array[pivot]
            return pivot

        if end is None: end = len(array) - 1

        def _quicksort(array, begin, end):
            if begin >= end:
                return
            pivot = partition(array, begin, end)
            _quicksort(array, begin, pivot - 1)
            _quicksort(array, pivot + 1, end)

        return _quicksort(array, begin, end)

    def flip(self, nums, s, e):
        li, ri = s, e
        while li<ri: nums[ri], nums[li], li, ri = nums[li], nums[ri],li+1,ri-1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if N < 2: return
        idx = N - 2
        while idx >= 0 and nums[idx] >= nums[idx + 1]: idx -= 1
        idy, minidy = idx + 1, idx + 1
        for idy in range(idx + 1, N):
            if nums[minidy] > nums[idy] and nums[idy] > nums[idx]: minidy = idy

        nums[idx], nums[minidy] = nums[minidy], nums[idx]
        #self.quicksort(nums, idx + 1)
        self.flip(nums,idx+1,len(nums)-1)
a = [1,2,4,3,2,1]
Solution().nextPermutation(a)
print(a)
