#!/usr/bin/env python3
"""copet cat matrice"""


def cat_matrices2D(mat1, mat2, axis=0):
    """ cat mat 2d"""
    new = []
    lis = []
    if axis == 0 and (len(mat1[0]) == len(mat2[0])):
        return(mat1 + mat2)
    elif axis == 1 and (len(mat1) == len(mat2)):
        for i in range(len(mat1)):
            lis = mat1[i] + mat2[i]
            new.append(lis)
        return(new)
