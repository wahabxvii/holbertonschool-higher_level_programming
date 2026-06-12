#!/usr/bin/python3
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        print(" ".join(str(element) for element in row))


print_matrix_integer(matrix)
print("--")
print_matrix_integer()
