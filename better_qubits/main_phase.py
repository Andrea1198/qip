import numpy as np
from qubits import Qubit, Register

phase = 2

n = 2       # phase accuracy
m = 2       # Store u

u = Qubit(np.random.random())

control_reg = [Qubit(0.) for i in range(n)] + [u] * m 
control_reg = Register(control_reg)
for i in range(n):
    control_reg.qubits[i].H_gate()

k = 0
for i in range(n-1,-1,-1):
    control_reg.qubits[i].print()
    qubit = control_reg.qubits[i]
    qubit.C_U_gate(k, phase)
    control_reg.modify_qubit(i, qubit)
    k += 1
print(phase)
for i in range(n):
    control_reg.qubits[i].print()