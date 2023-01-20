from qubit import Qubit, Register
import math as mt
from scipy.fft import fft, ifft
import numpy as np

n = 4
N = 2 ** n 

coeffs = []
for i in range(n):
    coeffs.append([np.random.randint(2)+0j,0+0j])

for i in range(len(coeffs)):
    coeffs[i][1] = 1 - coeffs[i][0]

def convert(coe):
    result = 0
    for i in range(len(coe)):
        pow = 2 ** i 
        result += coe[len(coe) - i - 1][1] * pow
    return result

state = convert(coeffs)
print(state)
initial = Register(coeffs)
initial.print()
print()

def F_operator(reg, state):
    for i, qubit in enumerate(reg.state):
        qubit.H_gate()
        k = 2
        for j in range(i+1, n):
            qubit.R_gate(reg.state[j], k)
            k += 1
    return reg

final = F_operator(initial, state)
final.print()