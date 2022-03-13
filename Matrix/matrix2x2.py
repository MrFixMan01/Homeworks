from matrix import Matrix


class Matrix2x2(Matrix):
    def __init__(self, matrix=[[0, 0], [0, 0]]):
        assert len(matrix) == 2
        assert len(matrix[0]) == 2
        assert len(matrix[1]) == 2

        self.strok = 2
        self.stolb = 2
        self.matrix = matrix

    def determinant(self):
        return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
