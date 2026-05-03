class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c, visited):
            ROWS, COL = len(grid), len(grid[0])
            if (min(r, c) < 0 or r == ROWS or c == COL or
                grid[r][c] == 1 or (r, c) in visited):
                return 0
            if r == ROWS - 1 and c == COL - 1:
                return 1

            visited.append((r, c))

            count = 0

            count += dfs(grid, r - 1, c, visited) # Left
            count += dfs(grid, r + 1, c, visited) # Right
            count += dfs(grid, r, c + 1, visited) # Up
            count += dfs(grid, r, c - 1, visited) # Down

            visited.remove((r, c))

            return count
        
        return dfs(grid, 0, 0, list())