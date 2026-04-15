class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_set = set()
        l = r = 0
        while r < len(nums):

            if r - l > k:
                num_set.remove(nums[l])
                l += 1
            if nums[r] in num_set:
                return True
            num_set.add(nums[r])
            r += 1
        return False