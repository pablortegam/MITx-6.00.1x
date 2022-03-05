def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    multi=1
    for i in range (0,exp):
        multi=multi*base
        i-=1
    return multi
