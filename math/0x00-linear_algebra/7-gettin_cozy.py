#!/usr/bin/env python3
"""
7. Gettin’ Cozy
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    7. Gettin’ Cozy
    """
    res = []
    if axis == 0 and (len(mat1[0]) == len(mat2[0])):
        return mat1 + mat2
    elif axis == 1  and (len(mat1) == len(mat2)):
        for i in range(len(mat1)):
            res = (mat1[i] + mat2[i])
    return res
