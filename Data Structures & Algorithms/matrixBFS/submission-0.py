from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        path_length = 0
        queue = deque()
        queue.append((0, 0))
        visited.add((0, 0))

        while queue:
            for i in range(len(queue)):
                current_spot = queue.popleft()
                current_row = current_spot[0]
                current_col = current_spot[1]
                if current_row == rows - 1 and current_col == cols - 1:
                    return path_length
                
                for move_row, move_col in neighbours:
                    new_spot = (move_row + current_row, move_col + current_col)
                    if (0 > new_spot[0] or new_spot[0] == rows or 0 > new_spot[1] 
                        or new_spot[1] == cols or new_spot in visited 
                        or grid[new_spot[0]][new_spot[1]] == 1):
                        continue
                    queue.append(new_spot)
                    visited.add(new_spot)
            path_length += 1
        
        return -1

