from qubit import Qubit, Register
import math as mt
from scipy.fft import fft, ifft
import numpy as np

n = 3
N = 2 ** n 
INV_SQRT2 = 1./mt.sqrt(2.)

# coeffs = []
# for i in range(n):
#     coeffs.append([np.random.randint(2)+0j,0+0j])

# for i in range(len(coeffs)):
#     coeffs[i][1] = 1 - coeffs[i][0]

def convert(coe):
    result = 0
    for i in range(len(coe)):
        pow = 2 ** i 
        result += coe[len(coe) - i - 1][1] * pow
    return result

def generate_coeff(num):
    coeffs = []
    for i in range(n-1,-1,-1):
        coeffs.append([0,num // (2 ** i)])
        num -= (num // (2 ** i)) * (2 ** i)

    for i in range(n):
        coeffs[i][0] = 1 - coeffs[i][1]

    coeffs = coeffs[::-1]
    return coeffs

def F_operator(reg):
    for i, qubit in enumerate(reg.state):
        qubit.H_gate()
        k = 2
        for j in range(i+1, n):
            qubit.R_gate(reg.state[j], k)
            k += 1
    return reg



f_coeff = np.random.random(N) + 0j
f_coeff = np.ones(N) * INV_SQRT2
transform = []


result = np.zeros(N, np.complex64)
for i in range(N):
    coeffs = generate_coeff(i)
    initial = Register(coeffs)

    # print("# Initial state:")
    initial.print()
    # print()

    # print("# Apply F operator")
    final = F_operator(initial)
    # final.print()
    # print("# Reverse order of qubits")
    # print("# Final")
    final.reverse()
    # final.print()
    # print()
    final.print()
    for j in range(N):
        coef = generate_coeff(j)
        for k in range(n):
            c = coef[k]
            if c[0] == 1:
                result[j] += final.state[k].c0 * f_coeff[j]
            else:
                result[j] += final.state[k].c1 * f_coeff[j]
    print(result)
# result = result * fft(f_coeff)

# print(result)
result_dft = fft(f_coeff)
print(result_dft)