class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def backtrack(candidates):
            if len(candidates) == len(nums):
                res.append(candidates.copy())
                return
            
            for num in nums:
                if num not in used:
                    candidates.append(num)
                    used.add(num)
                    backtrack(candidates)
                    candidates.pop()
                    used.remove(num)
        
        backtrack([])
        return res