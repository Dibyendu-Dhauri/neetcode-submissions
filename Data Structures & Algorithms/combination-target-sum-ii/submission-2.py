class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        subsets = []
        candidates.sort()
        def backtrack(total,index):
            if total > target:
                return
            if total == target:
                ans.append(subsets.copy())
                return
            
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                total += candidates[i]
                subsets.append(candidates[i])
                backtrack(total,i+1)
                
                total -= candidates[i]
                subsets.pop()
        
        backtrack(0,0)
        return ans