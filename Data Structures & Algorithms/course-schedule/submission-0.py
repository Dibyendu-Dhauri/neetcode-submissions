class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}

        for course,prerequisite in prerequisites:
            adjList[course].append(prerequisite)
        
        visit = set()
        def dfs(node):
            if node in visit:
                # detect cycle
                return False

            if adjList[node] == []:
                return True

            visit.add(node)
            for neighbour in adjList[node]:
                if not dfs(neighbour):
                    return False
            visit.remove(node)
            adjList[node] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True