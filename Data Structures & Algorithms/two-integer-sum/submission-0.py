class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_num = defaultdict()

        for i,num in enumerate(nums):
            find_num = target - num
            if find_num in map_num:
                return [map_num[find_num],i]
            map_num[num] = i
