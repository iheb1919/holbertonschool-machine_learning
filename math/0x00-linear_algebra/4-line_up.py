#!/usr/bin/env python3
"""
4. Line Up
"""


def add_arrays(arr1, arr2):
    """
    4. Line Up
    """
    if len(arr1) != len(arr2):
        return None
    res = []
    for i in range(len(arr1)):
        res.append(arr1[i] + arr2[i])
    return res
