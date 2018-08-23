class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)<2: return 0
        prices = prices+[float('-inf')]
        idx, balance, hold_idx = 0, 0, None
        for idx in range(len(prices)-1):
            if hold_idx is None and prices[idx] < prices[idx+1]: balance, hold_idx = balance - prices[idx], idx
            elif hold_idx is not None and prices[idx] >= prices[idx+1]: balance, hold_idx = balance + prices[idx], None
        return balance

print(Solution().maxProfit([2,2,5]))
print(Solution().maxProfit([1,1,1,0]))
print(Solution().maxProfit([7,6,5,4,3,2,1]))
print(Solution().maxProfit([1,7,6,5,4,3,2,1]))
print(Solution().maxProfit([1,3,7,5,4,3,2,1]))
print(Solution().maxProfit([1,3,7,5,4,3,2,10]))