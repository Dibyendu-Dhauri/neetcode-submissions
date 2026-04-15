class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0
        fresh = 0
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dirs:
                    nrow,ncol = dr + r, dc + c
                    if (nrow in range(len(grid)) and ncol in range(len(grid[0]))
                    and grid[nrow][ncol] == 1):
                        grid[nrow][ncol] = 2
                        q.append((nrow,ncol))
                        fresh -= 1

            time += 1
        
        return time if fresh == 0 else -1
