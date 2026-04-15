class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}
        ans = 0
        visit = set()
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(node):
            if node in visit:
                return 
            
            visit.add(node)

            for nei in adjList[node]:
                dfs(nei)

        for i in range(n):
            if i not in visit:
                dfs(i)
                ans += 1
        
        return ans