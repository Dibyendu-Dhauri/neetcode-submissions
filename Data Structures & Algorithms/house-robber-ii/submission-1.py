class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob1(nums: List[int]) -> int:
            rob1, rob2 = 0, 0
            
            for num in nums:
                current = max(rob2, rob1+num)
                rob1 = rob2
                rob2 = current
            return rob2

        return max(rob1(nums[1:]), rob1(nums[:-1]))
        