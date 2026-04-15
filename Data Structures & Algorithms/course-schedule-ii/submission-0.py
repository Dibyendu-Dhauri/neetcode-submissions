class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        q = deque()
        ans = []

        for src,dst in prerequisites:
            adjList[src].append(dst)
            indegree[dst] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            ans.append(node)
            for nei in adjList[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return ans[::-1] if len(ans) == numCourses else []