#!/usr/bin/env python3
""" poly_integral"""


def poly_integral(poly, C=0):
    """ poly_integral"""
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
