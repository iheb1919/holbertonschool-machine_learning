#!/usr/bin/env python3
"""
"""


def matrix_shape(matrix):
    """
    """
    size = []
    while matrix:
        if type(matrix) is list:
            size.append(len(matrix))
            matrix = matrix[0]
        else:
            break
    return size
