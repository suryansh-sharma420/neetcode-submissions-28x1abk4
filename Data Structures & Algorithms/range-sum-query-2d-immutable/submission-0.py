class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #starting point is r1,c1 so traverse till there, and sum is only of that box
        #ex: 2,1 to 4,3 goes --> 2,1 - 2,2 - 2,3 so column from 1 to 3, and rows from 2 to 4, and sum each
        self.summation = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.summation += self.matrix[i][j]
        return self.summation



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)