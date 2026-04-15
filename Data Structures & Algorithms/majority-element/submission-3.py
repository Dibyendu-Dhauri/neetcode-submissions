class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = res = 0
        for i in range(len(nums)):
            if count == 0:
                res = nums[i]
            count += (1 if res == nums[i] else -1)
        return res