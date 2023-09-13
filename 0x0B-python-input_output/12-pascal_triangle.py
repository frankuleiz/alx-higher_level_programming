#!/usr/bin/python3
"""The ``12-pascal_triangle``module"""


def pascal_triangle(n):
    """A function to print a pascal triangle"""
    if n <= 0:
        return []

    pascal = [[1]]
    for x in range(1, n):
        row = [1]
        if x > 1:
            for i in range(1, len(pascal[x - 1])):
                row.append(pascal[x - 1][i - 1] + pascal[x - 1][i])
        row.append(1)
        pascal.append(row)

    return pascal
