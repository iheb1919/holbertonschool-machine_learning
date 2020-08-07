#!/usr/bin/env python3
"""
python
"""


def poly_derivative(poly):
    """sd"""
    if type(poly) is not list:
        return(None)
    if len(poly) == 0:
        return(None)
    if len(poly) == 1:
        return([0])
    res = []
    for i in range(len(poly)):
        if i != 0:
            res.append(i * poly[i])
    return(res)
