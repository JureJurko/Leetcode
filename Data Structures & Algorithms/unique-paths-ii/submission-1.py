class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        num_of_rows = len(obstacleGrid) 
        num_of_cols = len(obstacleGrid[0])
        
        if obstacleGrid[num_of_rows-1][num_of_cols-1] == 1:
            return 0
            
        prev_row = [0] * num_of_cols

        for row in range(num_of_rows - 1, -1, -1):
            curr_row = [0] * num_of_cols
            
            for col in range(num_of_cols - 1, -1, -1):
                if obstacleGrid[row][col] == 1:
                    curr_row[col] = 0
                elif row == num_of_rows - 1 and col == num_of_cols - 1:
                    curr_row[col] = 1
                else:
                    down = prev_row[col]
                    right = curr_row[col + 1] if col + 1 < num_of_cols else 0
                    curr_row[col] = down + right

            prev_row = curr_row
        
        return prev_row[0]