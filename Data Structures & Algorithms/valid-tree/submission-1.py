class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(n)}
        visit = set()

        for src,dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)

        
        def dfs(node,previous_node):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adjList[node]:
                if nei == previous_node:
                    continue
                if not dfs(nei,node):
                    return False
            
            
            return True
        
        return dfs(0,-1) and len(visit) == n