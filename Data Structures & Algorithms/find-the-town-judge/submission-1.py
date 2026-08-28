class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        judge = [0] * (n + 1)

        for a,b in trust:
            judge[b] += 1
            judge[a] -= 1
        
        for i in range(1,len(judge)):
            if judge[i] == n-1:
                return i

        return -1