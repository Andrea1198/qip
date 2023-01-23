import numpy as np

def qft(register):
    n = len(register.qubits)
    for i in range(n):
        qubit = register.qubits[i]
        qubit.H_gate()
        k = 2
        for j in range(i+1, n):
            control = register.qubits[j]
            qubit.R_gate(k, control)
            k += 1
        register.modify_qubit(i, qubit)
    register.invert_qubits()
    return register