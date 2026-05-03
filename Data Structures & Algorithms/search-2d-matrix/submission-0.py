class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1

        found_range = False
        while left <= right:
            middle_row = (left + right) // 2

            if target > matrix[middle_row][-1]:
                left = middle_row + 1
            elif target < matrix[middle_row][0]:
                right = middle_row - 1
            else:
                found_range = True
                break
        
        if not found_range:
            return False
        
        left, right = 0, len(matrix[middle_row]) - 1
        while left <= right:
            middle_column = (left + right) // 2

            if target > matrix[middle_row][middle_column]:
                left = middle_column + 1
            elif target < matrix[middle_row][middle_column]:
                right = middle_column - 1
            else:
                return True
        
        return False
        

        

