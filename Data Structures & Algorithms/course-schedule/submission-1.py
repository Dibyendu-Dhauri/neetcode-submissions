class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        q = deque()

        for src,dst in prerequisites:
            indegree[dst] += 1
            adjList[src].append(dst)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        finish = 0

        while q:
            node = q.popleft()
            finish += 1
            for neighbour in adjList[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        
        return finish == numCourses