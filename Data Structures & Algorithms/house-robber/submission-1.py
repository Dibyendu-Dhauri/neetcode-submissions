class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)

        prev_prev_profit = nums[0]
        prev_profit = max(nums[0], nums[1])

        for i in range(2,len(nums)):
            current = max(prev_profit, nums[i] + prev_prev_profit)
            prev_prev_profit = prev_profit
            prev_profit = current

        return prev_profit