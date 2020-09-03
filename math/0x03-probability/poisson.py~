#!/usr/bin/env python3
""" class poisson that represents a poisson distribution"""




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
