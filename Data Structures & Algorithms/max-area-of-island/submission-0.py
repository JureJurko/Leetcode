class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(grid, r, c):
            if (min(r, c) < 0 or r == rows or c == cols
                or grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0
            island_size = 1
            
            island_size += dfs(grid, r - 1, c)
            island_size += dfs(grid, r + 1, c)
            island_size += dfs(grid, r, c - 1)
            island_size += dfs(grid, r, c + 1)

            return island_size
        
        return max(
            [dfs(grid, i, j) 
             for i in range(len(grid)) 
             for j in range(len(grid[0])) 
             if grid[i][j] == 1],
            default=0
        )
