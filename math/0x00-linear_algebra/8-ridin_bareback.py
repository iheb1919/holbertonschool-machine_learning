#!/usr/bin/env python3
"""
"""


def mat_mul(mat1, mat2):
    """
    """
    res = []
    if len(mat1[0]) != len(mat2):
        return None
    for i in range(len(mat1)):
        res.append([])
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            for k in range(len(mat2[0])):
                res[i][k].append(mat1[i][j] * mat2[j][k])
    return res
