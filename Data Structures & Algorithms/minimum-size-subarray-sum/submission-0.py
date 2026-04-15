class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        total_sum = 0
        ans = float('inf')
        while r < len(nums):
            total_sum += nums[r]
            while total_sum >= target:
                ans = min(ans, r - l + 1)
                total_sum -= nums[l]
                l += 1
            r += 1
        return ans if ans != float('inf') else 0