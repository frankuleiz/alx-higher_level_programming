def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for i in range(len(matrix)):
        new_matrix[row] = list(map(lambda x: x ** 2, new_matrix[row]))
    return new_matrix
