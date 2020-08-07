def summation_i_squared(n):
    """sum """
    if n is None or n < 1:
        return None
    res = list(map(lambda x: x**2, list(range(1, n+1))))
    return sum(res)
