#!/usr/bin/env python3
""" add matrix"""


def matrix_shape(matrix):
    """
    2. Size Me Please
    """
    size = []
    while matrix:
        if type(matrix) is list:
            size.append(len(matrix))
            matrix = matrix[0]
        else:
            break
    return size


def add_matrices(mat1, mat2):
    """add two matrix"""
    res = []
    size1 = matrix_shape(mat1)
    size2 = matrix_shape(mat2)
    if (size1 != size2):
        return(None)
    if len(size1) == 1:
        for i in range(size1[0]):
            s = mat1[i] + mat2[i]
            res.append(s)
    else:
        for matrix1, matrix2 in zip(mat1, mat2):
            res.append(add_matrices(matrix1, matrix2))
    return(res)
