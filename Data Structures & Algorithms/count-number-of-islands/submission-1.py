class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        
        def dfs(r,c):
            
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '1':
                grid[r][c] = -1
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dfs(r,c)
                    cnt += 1
        
        return cnt