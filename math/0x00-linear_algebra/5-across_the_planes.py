#!/usr/bin/env python3
"""
"""


def add_matrices2D(mat1, mat2):
    """
    """
    if len(mat1) != len(mat2):
        return None
    res = []
    for i in range(len(mat1)):
        if (len(mat1[i]) != len(mat2[i])):
            return None
        else:
            res.append([])
            for j in range(len(mat1[i])):
                res[i].append(mat1[i][j] + mat2[i][j])
    return res
