class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r  = 0
        ans = 0
        while r < len(prices):

            while prices[r] < prices[l]:
                l += 1

            ans = max(ans,prices[r] - prices[l])
            r += 1
        return ans