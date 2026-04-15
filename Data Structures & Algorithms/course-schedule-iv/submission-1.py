class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList ={i: [] for i in range(numCourses)}
        output = []
        for src,dst in prerequisites:
            adjList[src].append(dst)
        
        def dfs(node,dst,visit):
            if node == dst:
                return True
            
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adjList[node]:
                if dfs(nei,dst,visit):
                    return True
            return False

        for src,dst in queries:
            output.append(dfs(src,dst,set()))
        
        return output