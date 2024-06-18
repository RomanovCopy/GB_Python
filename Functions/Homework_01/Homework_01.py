# Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix, и возвращает транспонированную матрицу.

# Пример использования На входе:


matrix = [[1, 2, 3],
         [4, 5, 6], 
         [7, 8, 9]]
# transposed_matrix = transpose(matrix)
# На выходе:


# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

def transpose_matrix(matrix):
    """
    Функция для транспонирования матрицы.

    Аргументы:
    matrix (list of list): Исходная матрица.

    Возвращает:
    list of list: Транспонированная матрица.
    """
    # Получаем количество строк и столбцов исходной матрицы
    rows = len(matrix)
    cols = len(matrix[0])

    # Создаем новую матрицу для хранения транспонированной матрицы
    transposed_matrix = [[0] * rows for _ in range(cols)]

    # Заполняем значениями из исходной матрицы
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


print(transpose_matrix(matrix))