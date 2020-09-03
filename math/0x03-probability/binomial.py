#!/usr/bin/env python3
""" class Exponential"""


e = 2.7182818285


def factorial(n):
    """ return n!"""
    if n == 0:
        return 1
    total = 1
    for i in range(1, n + 1):
        total = total * i
    return total


class Binomial():
    """ Class to calculate Exponential distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """Constructor of Binomial
        """

        if data is None:
            self.p = float(p)
            self.n = int(n)
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
        else:
            if isinstance(data, list):
                if len(data) < 2:
                    raise ValueError("data must contain multiple values")
                else:
                    self.data = data
                    mean = sum(self.data) / len(self.data)
                    nd = 0
                    for i in data:
                        nd = nd + ((i - mean) ** 2)
                    summ = (nd / len(data)) ** 0.5
                    var = summ ** 2
                    p = 1 - var / mean
                    self.n = int(round(mean / p))
                    self.p = mean / self.n
            else:
                raise TypeError("data must be a list")

    def factorial(x):
        """ return n!"""
        if x == 0:
            return 1
        fact = 1
        for i in range(1, x + 1):
            fact = fact * i
        return fact

    def pmf(self, k):
        """ Binomial PMF"""
        k = int(k)
        if k < 0:
            return 0
        fac = factorial(int(self.n)) / (factorial(k) *
                                        factorial(int(self.n) - k))
        return fac * (self.p ** k) * ((1 - self.p) ** (int(self.n) - k))

    def cdf(self, k):
        """ Binomial CDF"""
        k = int(k)
        if k < 0:
            return 0
        cdf = 0
        for i in range(k + 1):
            cdf = cdf + self.pmf(i)
        return cdf
