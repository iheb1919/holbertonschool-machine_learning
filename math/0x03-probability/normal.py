#!/usr/bin/env python3
""" Initialize Normal"""

pi = 3.1415926536
e = 2.7182818285


class Normal():
    """ class Normal that represents a normal distribution"""

    def __init__(self, data=None, mean=0, stddev=1.):
        """Constructor"""
        self.stddev = float(stddev)
        self.mean = float(mean)
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
        else:
            if isinstance(data, list):
                if len(data) > 1:
                    self.data = data
                    self.mean = float(sum(self.data) / len(self.data))
                    numerador = 0
                    for item in data:
                        numerador = numerador + ((item - self.mean) ** 2)
                    self.stddev = (numerador / len(data)) ** 0.5
                else:
                    raise ValueError("data must contain multiple values")
            else:
                raise TypeError("data must be a list")

    def z_score(self, x):
        """ normalize normal"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """x_value"""
        return z * self.stddev + self.mean

    def pdf(self, x):
        """normal PDF"""
        p = (self.z_score(x)) ** 2
        return (1 / (self.stddev * ((2 * pi)**0.5)) * (e ** ((-0.5) * p)))

    def cdf(self, x):
        """ normal cdf"""
        xx = (self.z_score(x)) / (2 ** 0.5)
        xxx = (2 / (pi ** 0.5)) * (xx - (xx ** 3) / 3 + (xx ** 5) / 10 -
                                   (xx ** 7) / 42 + (xx ** 9) / 216)
        cdf = (0.5) * (1 + xxx)
        return cdf
