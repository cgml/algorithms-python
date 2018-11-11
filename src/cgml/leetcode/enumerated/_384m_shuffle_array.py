import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums, self.shuffled = nums, None

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.shuffled = None
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        if self.shuffled: return self.shuffled
        self.shuffled = list(self.nums)
        for idx in range(len(self.nums))[::-1]:
            idy = random.randint(0, idx)
            self.shuffled[idx], self.shuffled[idy] = self.shuffled[idy], self.shuffled[idx]
        return self.shuffled

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()