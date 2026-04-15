class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        for num in nums:
            mp[num] = mp.get(num,0) + 1
            if mp[num] > len(nums)/2:
                return num