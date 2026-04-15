class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}
        for num in nums:
            nums_map[num] = nums_map.get(num,0) + 1
            if nums_map[num] > 1:
                return True
        return False