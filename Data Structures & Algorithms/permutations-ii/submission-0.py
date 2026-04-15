from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = Counter(nums)

        def backtrack(candidates):
            if len(candidates) == len(nums):
                res.append(candidates.copy())
                return
            
            for num in count:
                if count[num] > 0:
                    candidates.append(num)
                    count[num] -= 1
                    backtrack(candidates)
                    candidates.pop()
                    count[num] += 1
        
        backtrack([])
        return res