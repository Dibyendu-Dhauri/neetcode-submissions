class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans =[]
        subsets = []

        def backtrack(index):
            if len(subsets) == k:
                ans.append(subsets.copy())
                return

            for i in range(index,n+1):
                subsets.append(i)
                backtrack(i+1)
                subsets.pop()
        
        backtrack(1)
        return ans