#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """
    function computes the square value of all integers of a matrix using map
    matrix is a 2 dimensional array
    Returns a new matrix
    """
    return list(map(lambda y: list(map(lambda x: x ** 2, y)), matrix))
