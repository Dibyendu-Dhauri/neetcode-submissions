from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            if len(count) <= 2:
                continue
            
            temp_count = defaultdict(int)
            for key,val in count.items():
                if val > 1:
                    temp_count[key] = val -1
            count = temp_count
        
        res = []
        for key,val in count.items():
            if nums.count(key) > len(nums) // 3:
                res.append(key)
        return res