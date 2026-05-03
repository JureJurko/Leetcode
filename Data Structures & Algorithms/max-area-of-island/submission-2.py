class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def _get_valid_neighbors(r: int, c: int):
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 
                    0 <= nc < cols and 
                    grid[nr][nc] == 1 and 
                    (nr, nc) not in visited):
                    yield nr, nc

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    current_area = 0
                    stack = [(r, c)]
                    visited.add((r, c))

                    while stack:
                        curr_r, curr_c = stack.pop()
                        current_area += 1
                        
                        for nr, nc in _get_valid_neighbors(curr_r, curr_c):
                            visited.add((nr, nc))
                            stack.append((nr, nc))
                    
                    if current_area > max_area:
                        max_area = current_area
                        
        return max_area