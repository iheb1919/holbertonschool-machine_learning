#!/usr/bin/env python3
""" poly_integral"""


def poly_integral(poly, C=0):
    """ poly_integral"""

    if isinstance(poly, list):
        return None
    if poly is None or len(poly) == 0:
        return None
    if(type(C) is not int):
        return None
    if(poly == [0]):
        return [C]
    res = [C]
    for i in range(len(poly)):
        inte = (poly[i] ** i) / (i + 1)
        if i == 0:
            res.append(poly[i])
        elif inte.is_integer():
            res.append(int(inte))
        else:
            res.append(inte)
    return res
