#!/usr/bin/env python3
"""
2. Size Me Please
"""


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
