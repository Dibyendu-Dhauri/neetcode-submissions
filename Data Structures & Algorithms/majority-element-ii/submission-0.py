from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp = Counter(nums)

        ans = []
        for key,val in mp.items():
            
            if val > len(nums) // 3:
                ans.append(key)
        return ans