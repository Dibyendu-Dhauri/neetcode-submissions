class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        INF = 2147483647
        visit = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visit.add((r,c))
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        dist = 0
        def is_within_bound(r,c):
            return 0 <= r < len(grid) and 0<= c < len(grid[0])
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = dist
                for dr,dc in dirs:
                    nr,nc = dr + r, dc + c
                    if is_within_bound(nr,nc) and (nr,nc) not in visit and grid[nr][nc] != -1:
                        queue.append((nr,nc))
                        visit.add((nr,nc))
            dist += 1