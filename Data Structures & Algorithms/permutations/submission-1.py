class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = Counter(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in count:              # 👈 key fix
                if count[num] > 0:
                    path.append(num)
                    count[num] -= 1
                    backtrack(path)
                    path.pop()
                    count[num] += 1

        backtrack([])
        return res