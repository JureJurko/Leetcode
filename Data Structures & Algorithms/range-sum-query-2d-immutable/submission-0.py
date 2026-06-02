class NumMatrix:
    def _initialize_pre_sum(self):
        for i, row in enumerate(self.matrix):
            self.pre_sum.append([])
            for j, element in enumerate(row):
                if j == 0:
                    self.pre_sum[i].append(element)
                else:
                    self.pre_sum[i].append(element + self.pre_sum[i][j - 1])

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.pre_sum = []

        self._initialize_pre_sum()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row2 - row1 + 1):
            if col1 > 0:
                total += self.pre_sum[i + row1][col2] - self.pre_sum[i + row1][col1 - 1]
            else:
                total += self.pre_sum[i + row1][col2]

        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)