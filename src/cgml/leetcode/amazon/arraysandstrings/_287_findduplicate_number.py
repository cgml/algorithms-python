class Solution:
    def findDuplicate(self, nums):
        slow, fast, finder = nums[0], nums[nums[0]], 0
        while slow != fast: slow, fast = nums[slow], nums[nums[fast]]
        while slow != finder: slow, finder = nums[slow], nums[finder]
        return slow


assert Solution().findDuplicate([4,3,2,1,2]) == 2

'''
TODO - Binary Search
public int findDuplicate(int[] nums) {
	int low = 1, high = nums.length - 1;
    while (low <= high) {
        int mid = (int) (low + (high - low) * 0.5);
        int cnt = 0;
        for (int a : nums) {
            if (a <= mid) ++cnt;
        }
        if (cnt <= mid) low = mid + 1;
        else high = mid - 1;
    }
    return low;
}

'''