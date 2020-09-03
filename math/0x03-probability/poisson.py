#!/usr/bin/env python3
""" class poisson that represents a poisson distribution"""

e = 2.7182818285

class Poisson():
    """ calculate Poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """Constructor"""
        self.lambtha = float(lambtha)
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        else:
            if isinstance(data, list):
                if len(data) > 1:
                    self.data = data
                    self.lambtha = float(sum(self.data) / len(self.data))
                else:
                    raise ValueError("data must contain multiple values")
            else:
                raise TypeError("data must be a list")


            def pmf(self, k):
                """ Calculates the PMF of the distribution.
                """
                k2 = int(k)
                if k2 < 0:
                    return 0
                else:
                    fact = 1
                    for i in range(1, x + 1):
                        fact = fact * i
                        res = e ** -self.lambtha * self.lambtha ** x / x_fact
                    return res
