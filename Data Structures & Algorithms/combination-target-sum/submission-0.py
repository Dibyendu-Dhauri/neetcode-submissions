class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        subsets = []

        def backtrack(total,index):
            if total > target:
                return
            if total == target:
                ans.append(subsets.copy())
                return
            
            for i in range(index,len(nums)):
                total += nums[i]
                subsets.append(nums[i])
                backtrack(total,i)
                total -= nums[i]
                subsets.pop()
        backtrack(0,0)
        return ans