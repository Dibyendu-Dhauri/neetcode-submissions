class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build and adj List from the given I/P
        # 2. Find out the In-degree of each course
        
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        queue = deque()
        enrolled_course = 0

        for a,b in prerequisites:
            graph[a].append(b)
            in_degree[b] += 1

        # 3. If and couses has 0 In-degree, push it into queue, to start the traversal
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            enrolled_course += 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                # If the in-degree of a neighboring course becomes 0, add it to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        # return true if we've successfully enrolled in all courses.
        return enrolled_course == numCourses