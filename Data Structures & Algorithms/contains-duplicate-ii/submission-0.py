class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_map = {}

        for i in range(len(nums)):

            if nums[i] in nums_map and abs(i - nums_map[nums[i]]) <= k:
                return True

            nums_map[nums[i]] = i
        return False