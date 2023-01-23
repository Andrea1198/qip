from qubits import Qubit, Register
import numpy as np
from library import generate_coeff
from qft import qft
from scipy.fft import fft


n = 4
N = 2 ** n
coeffs_f = np.ones(N) + 0.j
coeffs_f = np.random.random(N) + 0.j
coeffs_tr= np.zeros(N) + 0.j
coeffs_fft = fft(coeffs_f)
for i in range(N):
    coeffs = generate_coeff(i, n)
    qubits = []
    for coef in coeffs:
        qubits.append(Qubit(coef*np.pi))
    reg = Register(qubits)
    transf = qft(reg)
    for j in range(N):
        coeffs_tr[j] += coeffs_f[i] * transf.coeffs[j]
        # print(transf.qubits[j].c0, transf.qubits[j].c1)

print(coeffs_tr * np.sqrt(N))
print()
print(coeffs_fft)
print()
# print(coeffs_tr / coeffs_fft)
# print(coeffs_f / coeffs_fft)