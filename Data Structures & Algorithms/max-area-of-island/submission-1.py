class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (min(r, c) < 0 or r == rows or c == cols
                or grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0
            
            return 1 + sum(dfs(r + dr, c + dc) 
                        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)))
        
        return max(
            [dfs(i, j) 
             for i in range(len(grid)) 
             for j in range(len(grid[0])) 
             if grid[i][j] == 1],
            default=0
        )
