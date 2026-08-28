class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visited = set()

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(r,c):
            
            if(r< 0 or r >= len(grid)) or ( c < 0 or c >= len(grid[0])) or (grid[r][c] == 0):
                return 1
            ans = 0
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            for dr,dc in dirs:
                nr,nc = dr+r, dc + c
                if (nr,nc) not in visited:
                    ans += dfs(nr,nc)
            return ans

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row,col) not in visited:
                    return dfs(row,col)