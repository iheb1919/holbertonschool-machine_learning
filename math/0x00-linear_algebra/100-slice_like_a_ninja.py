#!/usr/bin/env python3
"""slice like a ninja"""


def np_slice(matrix, axes={}):
    """slice like a ninja"""
    lis = []
    for i in range(len(matrix.shape)):
        t = slice(*axes.get(i, (None, None)))
        lis.append(t)
    return(matrix[tuple(lis)])
