class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        q = deque()
        distance = 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dirs:
                    nr,nc = dr + r, dc + c
                    if (0<= nr < len(grid) and 0<= nc < len(grid[0]) and grid[nr][nc] == INF):
                        q.append((nr,nc))
                        grid[nr][nc] = distance
            
            distance += 1