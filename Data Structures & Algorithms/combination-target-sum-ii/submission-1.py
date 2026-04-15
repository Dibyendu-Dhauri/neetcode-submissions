class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        subsets = []
        candidates.sort()
        def backtrack(total,index):
            if total > target:
                return
            if total == target and subsets not in ans:
                ans.append(subsets.copy())
                return
            
            for i in range(index,len(candidates)):
                
                total += candidates[i]
                subsets.append(candidates[i])
                backtrack(total,i+1)
                while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                    i += 1
                total -= candidates[i]
                subsets.pop()
        
        backtrack(0,0)
        return ans