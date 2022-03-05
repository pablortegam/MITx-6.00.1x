def polysum(n, s):
    '''
    n, s: positive integers
    'n' is the number of sides and 's' is each side´s length
    returns: the square of the perimeter plus the area of a regular polygon rounded
    to four decimals places.
    '''
    #import math library for trigonometry functions and pi definition.
    import math
    #computes the area of the polygon
    area=(0.25*n*s**2)/(math.tan(math.pi/n))
    #computes the peremiter
    peri=n*s
    #computes the polysum function
    sum=area+peri**2
    #returns answer rounded to 4 decimals
    return round(sum,4)
