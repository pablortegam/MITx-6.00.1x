def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    smaller=min(a,b)
    larger=max(a,b)
    if smaller == 0:
        return larger
    else:
        return gcdRecur(smaller,larger%smaller)
