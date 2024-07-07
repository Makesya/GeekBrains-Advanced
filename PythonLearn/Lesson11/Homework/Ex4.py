
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        result = ""
        for row in self.data:
            result += " ".join(map(str, row)) + "\n"
        result = result[:-1]
        return result

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __eq__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.data[i][j] != other.data[i][j]:
                        return False
            return True
        return False

    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result

    def __mul__(self, other):
        if self.cols == other.rows:
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    sum = 0
                    for k in range(self.cols):
                        sum += self.data[i][k] * other.data[k][j]
                    result.data[i][j] = sum
            return result


# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)
