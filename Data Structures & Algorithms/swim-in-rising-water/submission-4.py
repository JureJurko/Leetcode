from collections import defaultdict

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        finish = (len(grid) - 1, len(grid) - 1)

        for i in range(len(grid)):
            for j in range(len(grid)):
                curr_edge = grid[i][j]
                neighboring_right = grid[i][j + 1] if len(grid) > j +1 else None
                neighboring_down = grid[i + 1][j] if len(grid) > i +1 else None
                neighboring_left = grid[i][j - 1] if j - 1 >= 0 else None
                neighbor_up = grid[i - 1][j] if i - 1 >= 0 else None

                if neighboring_right is not None and neighboring_right <= curr_edge:
                    neighbors[(i, j)].append([(i, j + 1), 0])
                elif neighboring_right is not None:
                    neighbors[(i, j)].append([(i, j + 1), neighboring_right - curr_edge])
                
                if neighboring_down is not None and neighboring_down <= curr_edge:
                    neighbors[(i, j)].append([(i + 1, j), 0])
                elif neighboring_down is not None:
                    neighbors[(i, j)].append([(i + 1, j), neighboring_down - curr_edge])

                if neighboring_left is not None and neighboring_left <= curr_edge:
                    neighbors[(i, j)].append([(i, j - 1), 0])
                elif neighboring_left is not None:
                    neighbors[(i, j)].append([(i, j - 1), neighboring_left - curr_edge])

                if neighbor_up is not None and neighbor_up <= curr_edge:
                    neighbors[(i, j)].append([(i - 1, j), 0])
                elif neighbor_up is not None:
                    neighbors[(i, j)].append([(i - 1, j), neighbor_up - curr_edge])
        
        shortest = {}
        min_heap = [[grid[0][0], (0, 0)]]
        while min_heap:
            w1, p1 = heapq.heappop(min_heap)
            if p1 in shortest:
                continue
            
            shortest[p1] = w1

            if finish in shortest:
                break

            for p2, w2 in neighbors[p1]:
                curr_elevation = grid[p1[0]][p1[1]]
                heapq.heappush(min_heap, [max(w1, curr_elevation + w2), p2])
        return shortest[finish]
            
                