import numpy as np

INV_SQRT2 = 1./np.sqrt(2.)

def generate_coeff(num, n):
    coeffs = []
    for i in range(n-1,-1,-1):
        coeffs.append(num // (2 ** i))
        num -= (num // (2 ** i)) * (2 ** i)

    # coeffs = coeffs[::-1]
    return coeffs

def mmul(a, b):
    # a (n, m), b(n) -> c(m)
    n = len(a)
    m = len(a[0])
    c = []
    for i in range(m):
        summ = 0
        for j in range(n):
            summ += a(i,j) * b(j)
        c.append(summ)
    return c
