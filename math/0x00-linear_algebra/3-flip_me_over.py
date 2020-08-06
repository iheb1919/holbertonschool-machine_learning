#!/usr/bin/env python3
"""
"""


def matrix_transpose(matrix):
    """
    """
    res = []
    for i in matrix[0]:
        res.append([])
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            res[i].append(matrix[j][i])
    return(res)
